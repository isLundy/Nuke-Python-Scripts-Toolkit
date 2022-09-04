"""This is the main module which contains the main defaults windows to create
and edit knob defaults."""


# Import built-in modules
import os
import shutil
import xml.etree.ElementTree as et

# Import third-party modules
# pylint: disable=import-error
import nuke

try:
    from PySide2 import QtWidgets
    from PySide2 import QtGui
    from PySide2 import QtCore
except ImportError:
    from PySide import QtGui as QtWidgets
    from PySide import QtGui
    from PySide import QtCore

# Import local modules
from default import helper
from default import templates


def create_default():
    """Create custom knob default value."""

    node = nuke.thisNode()
    knob = nuke.thisKnob()

    # Set default for current nuke session.
    key = "{}.{}".format(node.Class(), knob.name())
    nuke.knobDefault(key, str(knob.value()))

    # Write to knob_default_xml.
    helper.update_knob_defaults_xml(node.Class(), knob.name(),
                                    str(knob.value()), "append")


def reset_to_default():
    """Reset to standard knob default value."""

    node = nuke.thisNode()
    knob = nuke.thisKnob()

    knob.setValue(knob.defaultValue())
    key = "{}.{}".format(node.Class(), str(knob.name()))

    nuke.knobDefault(key, str(knob.defaultValue()))
    helper.update_knob_defaults_xml(node.Class(), knob.name(), "", "del")


def show_knob_list():
    """Show window for all knobs setting individual knob defaults."""

    try:
        sel = nuke.selectedNode()
    except ValueError:
        return None

    dict_all_knobs = sel.knobs()
    list_knobs = ["-----"]
    for name in dict_all_knobs.keys():
        if name not in helper.get_exclude_list():
            list_knobs.append(name)

    list_knobs.sort()

    panel = nuke.Panel("all knobs")
    panel.addEnumerationPulldown("knob", " ".join(list_knobs))
    panel.addSingleLineInput("new default value", "")
    if panel.show():
        # Set default for current nuke session.
        key = "{}.{}".format(sel.Class(), panel.value("knob"))
        nuke.knobDefault(key, panel.value("new default value"))

        # Update knob default in xml.
        helper.update_knob_defaults_xml(sel.Class(), panel.value("knob"),
                                        panel.value("new default value"),
                                        "append")


def show_defaults_window():
    """Show defaults panel. Make sure there exists only one notice_window panel
    present at a time. Close the panel if it already exists.

    Returns:
        DefaultsWindow: DefaultsWindow instance.
    """

    # pylint: disable=global-variable-undefined
    # pylint: disable=invalid-name
    global defaults_window

    try:
        defaults_window.close()
        del defaults_window
    except:
        pass

    defaults_window = DefaultsWindow()
    defaults_window.show()
    defaults_window.raise_()

    helper.center(defaults_window)
    return defaults_window


class DefaultsWindow(QtWidgets.QWidget):
    """This is the main window to set knob defaults."""

    def __init__(self):
        """Initialize the DefaultsWindow instance."""

        super(DefaultsWindow, self).__init__()

        self.setWindowTitle("default")
        self.resize(900, 600)
        self.knob_defaults_list = helper.load_knob_defaults()
        self.current_knobdefault_changed = False
        self.build_ui()

    def build_ui(self):
        """Build user interface."""

        self.create_widgets()
        self.create_layouts()
        self.create_signals()

    def create_widgets(self):
        """Create widgets."""
        self.combo_presets = QtWidgets.QComboBox()
        self.combo_presets.addItems(helper.list_presets())

        knob_defaults_xml = helper.get_current_knob_defaults_xml()
        cur_knob_defaults_name = os.path.basename(knob_defaults_xml)
        cur_knob_defaults_name = cur_knob_defaults_name.replace(".xml", "")

        self.combo_presets.setCurrentIndex(self.combo_presets.findText(
            cur_knob_defaults_name))

        self.push_preset_delete = QtWidgets.QPushButton("delete")
        self.push_preset_delete.setObjectName("push_red")
        self.push_preset_rename = QtWidgets.QPushButton("rename")
        self.push_preset_new = QtWidgets.QPushButton("new")
        self.push_preset_new.setObjectName("push_green")
        self.push_preset_import = QtWidgets.QPushButton("import preset")
        label_export = "export preset '{}'".format(
            self.combo_presets.currentText())
        self.push_preset_export = QtWidgets.QPushButton(label_export)

        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(5)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.load_defaults_to_table()

        self.push_close = QtWidgets.QPushButton("close")
        self.push_add_knob_default = QtWidgets.QPushButton(
            "add new knobDefault")
        self.push_add_knob_default.setObjectName("push_blue")

    def create_layouts(self):
        """Create layouts."""

        self.layout_top = QtWidgets.QHBoxLayout()
        self.layout_top.addWidget(self.combo_presets, 7)
        self.layout_top.addWidget(self.push_preset_delete, 1)
        self.layout_top.addWidget(self.push_preset_rename, 1)
        self.layout_top.addWidget(self.push_preset_new, 1)

        self.layout_import_export = QtWidgets.QHBoxLayout()
        self.layout_import_export.addWidget(self.push_preset_import)
        self.layout_import_export.addWidget(self.push_preset_export)

        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_main.addLayout(self.layout_top)
        self.layout_main.addLayout(self.layout_import_export)
        self.layout_main.addWidget(self.table)

        self.layout_push = QtWidgets.QHBoxLayout()
        self.layout_push.addWidget(self.push_add_knob_default)
        self.layout_push.addWidget(self.push_close)
        self.layout_main.addLayout(self.layout_push)

        self.setLayout(self.layout_main)
        helper.set_style_sheet(self)

    def create_signals(self):
        """Create signals."""

        self.push_close.clicked.connect(lambda: helper.close_(self))
        self.push_preset_delete.clicked.connect(self.delete_preset)
        self.push_preset_rename.clicked.connect(self.rename_preset)
        self.push_preset_new.clicked.connect(self.create_new_preset)
        self.push_add_knob_default.clicked.connect(
            lambda: self.show_edit_dialog("", "", "", "append"))
        self.combo_presets.currentIndexChanged.connect(self.set_current_preset)
        self.push_preset_import.clicked.connect(self.import_preset)
        self.push_preset_export.clicked.connect(self.export_preset)

    def import_preset(self):
        """Dialog to import a preset from disk."""

        dialog = QtWidgets.QFileDialog()
        dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        dialog.setWindowTitle("import preset")
        dialog.setNameFilter("preset xml(*.xml)")

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            selected_file = dialog.selectedFiles()[0]

            if not os.path.isfile(selected_file):
                nuke.message("Failed importing the preset. The file does not "
                             "exist.")
                return

            else:
                # check if the selected xml is a default preset xml
                # check by searching for "<defaults>" and "</defaults>"
                with open(selected_file, "r") as file_:
                    content = file_.read()

                    if not "<defaults>" in content:
                        msg = "The selected file '{}' is doesn't seem to be " \
                              "a defaults preset xml." \
                              "".format(os.path.basename(selected_file))
                        nuke.message(msg)
                        return

                    else:

                        preset_selected = os.path.basename(selected_file)
                        preset_name = preset_selected.replace(".xml", "")

                        root_current_xml = os.path.dirname(
                            helper.get_current_knob_defaults_xml())

                        import_file = os.path.join(
                            root_current_xml, preset_selected)

                        if os.path.isfile(import_file):
                            msg = "the preset '{}' already exists, do you " \
                                  "like to overwrite it?".format(preset_name)

                            if not nuke.ask(msg):
                                return

                        # Import file.
                        shutil.copy(selected_file, import_file)

                        # Append new preset to combo_presets.
                        self.combo_presets.addItems([preset_name])

                        # Reload defaults window.
                        def_window = show_defaults_window()
                        def_window.combo_presets.setCurrentIndex(
                            self.combo_presets.findText(preset_name))

    def export_preset(self):
        """Export preset to disk."""

        current_xml = "{}.xml".format(self.combo_presets.currentText())
        filename = QtWidgets.QFileDialog().getSaveFileName(
            self, "Save preset", "", os.path.expanduser("~/Desktop/"))
        filename = filename[0]

        if filename != "":
            # Get rid of extension.
            if "." in filename:
                filename = filename[0].split(".")[0]

            export = "{}.xml".format(filename)
            root_current_xml = os.path.dirname(
                helper.get_current_knob_defaults_xml())
            copy_from = os.path.join(root_current_xml, current_xml)

            if os.path.isfile(copy_from):
                if os.path.isfile(export):
                    if not nuke.ask("Overwrite '{}.xml'?".format(filename)):
                        return

                shutil.copy(copy_from, export)
                nuke.message("Successfully exported {} to:\n{}".format(
                    self.combo_presets.currentText(), export))
            else:
                nuke.message("An error occurred. Cannot find the preset xml "
                             "to export.")

    def create_new_preset(self):
        """Create new knob default preset."""

        inp = QtWidgets.QInputDialog()
        name, accept = inp.getText(self, "Create new preset",
                                   "name of new preset: ")

        if accept:
            # Cast some special characters.
            name = name.replace("/", "")
            name = name.replace(".", "")

            root_current_xml = os.path.dirname(
                helper.get_current_knob_defaults_xml())
            new_preset_xml = "{}/{}.xml".format(root_current_xml, name)

            if not os.path.isfile(new_preset_xml):
                with open(new_preset_xml, "w") as xml:
                    xml.write(templates.KNOB_DEFAULTS.strip())

                def_window = show_defaults_window()
                def_window.combo_presets.setCurrentIndex(
                    def_window.combo_presets.findText(name))
            else:
                nuke.message("The preset '{}' already exists. Please choose "
                             "a different name.".format(name))

    def load_defaults_to_table(self):
        """Loop through knobDefaults xml and populate table."""

        self.table.clear()
        self.table.setRowCount(len(self.knob_defaults_list))

        header_items = ["node", "knob", "value", "edit", "delete"]
        for collumn, name in enumerate(header_items):
            self.table.setHorizontalHeaderItem(
                collumn, QtWidgets.QTableWidgetItem(name))

        # Populate table
        for i, default, in enumerate(self.knob_defaults_list):
            self.populate_table(default, i)

    def set_default_list(self, def_list):
        """Set default list.

        Args:
            def_list (list): Defaults list to set.
        """

        self.knob_defaults_list = def_list

    def set_current_preset(self):
        """Write current preset to settings xml."""

        self.current_knobdefault_changed = True
        self.push_preset_export.setText("export preset '{}'".format(
            self.combo_presets.currentText()))

        settings_xml = helper.get_settings_xml()
        settings_tree = et.parse(settings_xml)
        settings_root = settings_tree.getroot()

        for child in settings_root.findall("set"):
            if child.get("name") == "cur_preset":
                child.text = "{}.xml".format(self.combo_presets.currentText())

        helper.prettyprint(settings_root)
        helper.write_xml(settings_xml, settings_root, settings_tree)

        helper.load_knob_defaults(init=True)
        self.knob_defaults_list = helper.load_knob_defaults()
        self.load_defaults_to_table()

    def rename_preset(self):
        """Rename preset."""

        inp = QtWidgets.QInputDialog()
        name, accept = inp.getText(self, "Rename preset",
                                   "Enter the new name for {}:".format(
                                       self.combo_presets.currentText()),
                                   text=self.combo_presets.currentText())

        if accept:
            # Cast some special characters.
            name = name.replace("/", "")
            name = name.replace(".", "")

            root_defaults_xml = os.path.dirname(
                helper.get_current_knob_defaults_xml())
            knob_xml = "{}.xml".format(self.combo_presets.currentText())
            orig_full_path = os.path.join(root_defaults_xml, knob_xml)
            renamed_full_path = os.path.join(root_defaults_xml,
                                             "{}.xml".format(name))

            if os.path.isfile(orig_full_path):
                os.rename(orig_full_path, renamed_full_path)

                def_window = show_defaults_window()
                def_window.combo_presets.setCurrentIndex(
                    def_window.combo_presets.findText(name))

                if os.path.isfile(orig_full_path):
                    os.remove(orig_full_path)

                def_window = show_defaults_window()
                def_window.combo_presets.setCurrentIndex(
                    def_window.combo_presets.findText(name))

            else:
                nuke.message("Error renaming the file. The file cannot be "
                             "found.")

    def delete_preset(self):
        """Delete selected preset."""

        root_xml = helper.get_root_current_xml()
        preset_delete = os.path.join(root_xml, "{}.xml".format(
            self.combo_presets.currentText()))

        message = "Do you really want to delete the preset '{}'? This can't " \
                  "be undone.".format(self.combo_presets.currentText())

        delete_label = "Delete preset '{}'".format(
            self.combo_presets.currentText())

        delete_preset = helper.ask_dialog(message,
                                          process_button_text=delete_label,
                                          color_process="60,0,0")

        if delete_preset:
            if os.path.isfile(preset_delete):
                os.remove(preset_delete)

                # Set current knob default xml to custom.
                settings_xml = helper.get_settings_xml()
                settings_tree = et.parse(settings_xml)
                settings_root = settings_tree.getroot()

                for child in settings_root.findall("set"):
                    if child.get("name") == "cur_preset":
                        child.text = "custom.xml"
                helper.prettyprint(settings_root)
                helper.write_xml(settings_xml, settings_root, settings_tree)

                show_defaults_window()
            else:
                nuke.message("An error occurred. The preset file doesn't "
                             "exist anymore.")

    def keyPressEvent(self, event):
        """Show restart window when closing window using escape key.

        Args:
            event (QtCore.QEvent): Event instance.
        """

        if event.key() == QtCore.Qt.Key_Escape:
            helper.close_(self)

    def populate_table(self, default, current_row):
        """populate table with knob default values from xml.

        Args:
            default (KnobDefault): Knob default instance.
            current_row (int): Current row to populate.
        """

        self.table.setItem(current_row, 0, QtWidgets.QTableWidgetItem(
            default.get_node()))
        self.table.setItem(current_row, 1, QtWidgets.QTableWidgetItem(
            default.get_knob()))
        self.table.setItem(current_row, 2, QtWidgets.QTableWidgetItem(
            default.get_value()))

        self.table.setColumnWidth(2, 360)

        # Edit
        push_edit = QtWidgets.QPushButton("edit")
        push_edit.setObjectName("{}___{}".format(default.get_node(),
                                                 default.get_knob()))
        self.table.setCellWidget(current_row, 3, push_edit)

        # Delete
        push_delete = QtWidgets.QPushButton("delete")
        style = "QPushButton { background-color: rgb(60, 0, 0);}"
        push_delete.setStyleSheet(style)
        push_delete.setObjectName("{}___{}___{}".format(default.get_node(),
                                                        default.get_knob(),
                                                        default.get_value()))

        self.table.setCellWidget(current_row, 4, push_delete)

        # Signals
        push_edit.clicked.connect(
            lambda: self.show_edit_dialog(default.get_node(),
                                          default.get_knob(),
                                          default.get_value(), "edit"))

        push_delete.clicked.connect(
            lambda: self.delete_knob_default(push_delete.objectName()))

    @staticmethod
    def delete_knob_default(meta):
        """Delete knob default from xml.

        Args:
            meta (str): Meta data to identify which data object to be removed
            from the xml.
        """

        node, knob, value = meta.split("___")
        knob_default_xml = helper.get_current_knob_defaults_xml()
        knob_defaults_tree = et.parse(knob_default_xml)
        knob_defaults_root = knob_defaults_tree.getroot()

        message = "Do you really want to delete the knob default" \
                  "\n'{}.{}={}' ? Please note: This can't be undone." \
                  "".format(node, knob, value)

        delete_default = helper.ask_dialog(
            message, process_button_text="Delete knob default",
            color_process="60,0,0")

        if delete_default:

            # Remove from xml.
            for child in knob_defaults_root.findall("default"):
                if child.get("node") == node and child.get("knob") == knob:
                    knob_defaults_root.remove(child)

            helper.prettyprint(knob_defaults_root)
            helper.write_xml(knob_default_xml, knob_defaults_root,
                             knob_defaults_tree)

            # Default knobDefault.
            # Create node, check default value and remove node.
            try:
                tmp = nuke.createNode("Blur", inpanel=False)
                tmp.setXYpos(-9999, -9999)
                tmp.setInput(0, None)
                tmp[knob].setValue(tmp[knob].defaultValue())
                default_value = tmp[knob].getValue()
                nuke.knobDefault("{}.{}".format(node, knob),
                                 "{}".format(default_value))
            except:
                pass

            # Reload defaults window.
            show_defaults_window()

    @staticmethod
    def show_edit_dialog(node, knob, value, mode):
        """Show edit dialog to change the knobDefault.

        Args:
            node (str): node name.
            knob (str): knob name.
            value (str): current knob default value.
        """

        # pylint: disable=global-variable-undefined
        # pylint: disable=invalid-name
        global edit_dialog
        edit_dialog = EditDialog(node, knob, value, mode)
        edit_dialog.show()
        edit_dialog.raise_()


class EditDialog(QtWidgets.QDialog):
    """Edit dialog window to edit and register a knob default to a new value.
    """

    def __init__(self, node, knob, value, mode):
        """Initialize the EditDialog instance.

        Args:
            node (str): node name.
            knob (str): knob name.
            value (str): current knob default value.
            mode (str): Mode to operate in ("edit", "new")
        """

        super(EditDialog, self).__init__()
        self.node = node
        self.knob = knob
        self.value = value
        self.mode = mode
        if self.mode == "edit":
            self.setWindowTitle("Edit knobValue '{}'".format(node))
        else:
            self.setWindowTitle("Add knobDefault")
        self.resize(QtCore.QSize(400, 120))
        self.build_ui()

    def build_ui(self):
        """Build user interface."""

        self.create_widgets()
        self.create_layouts()
        self.create_signals()

    def create_widgets(self):
        """Create widgets."""

        self.table = QtWidgets.QTableWidget()
        self.setStyleSheet("selection-background-color: transparent;")
        self.table.setFixedHeight(50)
        self.table.setRowCount(1)
        self.table.setColumnCount(3)
        self.table.horizontalHeader().setStretchLastSection(True)

        self.table.setHorizontalHeaderItem(
            0, QtWidgets.QTableWidgetItem("node"))
        self.table.setHorizontalHeaderItem(
            1, QtWidgets.QTableWidgetItem("knob"))
        self.table.setHorizontalHeaderItem(
            2, QtWidgets.QTableWidgetItem("value"))

        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem(self.node))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem(self.knob))
        self.table.setItem(0, 2, QtWidgets.QTableWidgetItem(self.value))

        self.push_check = QtWidgets.QPushButton("check validity")
        self.push_action = QtWidgets.QPushButton()
        if self.mode == "edit":
            self.push_action.setText("update knobDefault")
        else:
            self.push_action.setText("register knobDefault")
        self.push_cancel = QtWidgets.QPushButton("cancel")

    def create_layouts(self):
        """Create lyouts."""

        self.layout_push = QtWidgets.QHBoxLayout()
        self.layout_push.addWidget(self.push_action)
        self.layout_push.addWidget(self.push_check)
        self.layout_push.addWidget(self.push_cancel)

        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_main.addWidget(self.table)
        self.layout_main.addLayout(self.layout_push)

        self.setLayout(self.layout_main)

    def create_signals(self):
        """Create signals"""
        if self.mode == "edit":
            self.push_action.clicked.connect(self.update_knob_default)
        else:
            self.push_action.clicked.connect(self.append_knob_default)
        self.push_check.clicked.connect(self.show_validity_result)
        self.push_cancel.clicked.connect(self.close)

    def update_knob_default(self):
        """Update selected knobDefault in xml."""

        knob_default_xml = helper.get_current_knob_defaults_xml()
        knob_defaults_tree = et.parse(knob_default_xml)
        knob_defaults_root = knob_defaults_tree.getroot()

        # Update xml.
        for child in knob_defaults_root.findall("default"):
            if child.get("node") == self.node:
                if child.get("knob") == self.knob:
                    child.set("node", self.get_node_cur_value())
                    child.set("knob", self.get_knob_cur_value())
                    child.text = self.get_value_cur_value()

        helper.prettyprint(knob_defaults_root)
        helper.write_xml(knob_default_xml, knob_defaults_root,
                         knob_defaults_tree)

        key = "{}.{}".format(self.get_node_cur_value(),
                             self.get_knob_cur_value())
        nuke.knobDefault(key, self.get_value_cur_value())

        self.close()

        # Reload defaults window
        show_defaults_window()

    def append_knob_default(self):
        """Append new knob default to xml.

        Returns:
            Bool: True if successfuly appended knob defaullt, otherwise False.
        """

        node = self.get_node_cur_value()
        knob = self.get_knob_cur_value()
        value = self.get_value_cur_value()
        notice = ""

        if not node:
            notice = "Please enter a node\n"

        if not knob:
            notice = "Please enter a knob\n"

        if not value:
            notice = "Please enter a value.\n"

        if notice:
            notice = "An error occured.\n{}".format(notice)
            nuke.message(notice)
            return False

        try:
            helper.update_knob_defaults_xml(node, knob, value,
                                            "append")

            nuke.knobDefault("{}.{}".format(node, knob), value)
            nuke.message("successfully added new knob default:\n"
                         "\n{}.{} = {}".format(node, knob, value))

            self.close()

            # Reload defaults window.
            show_defaults_window()

            return True
        except Exception as error:
            nuke.message(str(error))
            return False

    def show_validity_result(self):
        """Show if the entered node and knob exists or not."""

        validity = self.check_validity()

        if validity["node"]:
            self.table.item(0, 0).setBackground(QtGui.QColor(50, 100, 50))
        else:
            self.table.item(0, 0).setBackground(QtGui.QColor(100, 50, 50))
            self.table.item(0, 1).setBackground(QtGui.QColor(100, 50, 50))

        if validity["node"] and not validity["knob"]:
            self.table.item(0, 1).setBackground(QtGui.QColor(100, 50, 50))
        if validity["node"] and validity["knob"]:
            self.table.item(0, 1).setBackground(QtGui.QColor(50, 100, 50))

        self.table.viewport().setFocusPolicy(QtCore.Qt.NoFocus)
        self.table.setFocusPolicy(QtCore.Qt.NoFocus)

    def check_validity(self):
        """Check if the entered knobDefault is valid.

        Returns:
            dict [Bool: node exists, Bool: knob exists]
        """

        node = self.get_node_cur_value()
        knob = self.get_knob_cur_value()

        validity = {}

        all_nodes = helper.get_all_nodes()
        if node in all_nodes and node != "":
            validity["node"] = True
            try:
                # Create temp node and check if the knob exists.
                tmp = nuke.createNode("{}".format(
                    self.table.item(0, 0).text()), inpanel=False)
                tmp.setXYpos(-9999, -9999)
                tmp.setInput(0, None)
                if knob != "":
                    try:
                        tmp[knob].getValue()
                        validity["knob"] = True
                    except NameError:
                        validity["knob"] = False
                    finally:
                        nuke.delete(tmp)
                else:
                    validity["knob"] = False
            except RuntimeError:
                validity["knob"] = False
        else:
            validity["node"] = False
            validity["knob"] = False

        self.table.setCurrentCell(0, 2)
        return validity

    def get_node_cur_value(self):
        """Get node value from table.

        Returns:
            str: Node value.
        """

        return self.table.item(0, 0).text()

    def get_knob_cur_value(self):
        """Get knob value from table.

        Returns:
            str: knob value.
        """

        return self.table.item(0, 1).text()

    def get_value_cur_value(self):
        """Get current default value from table.

        Returns:
            str: Current default value.
        """

        return self.table.item(0, 2).text()
