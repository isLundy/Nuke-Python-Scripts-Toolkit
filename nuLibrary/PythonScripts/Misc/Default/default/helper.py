"""This module contains helper functionality."""


# Import built-in modules
import os
from xml.etree import ElementTree

# Import third-party modules
# pylint: disable=import-error
import nuke

# Import local modules
from default import templates

try:
    from PySide2 import QtWidgets
    from PySide2 import QtCore
except ImportError:
    from PySide import QtGui as QtWidgets
    from PySide import QtCore


def set_style_sheet(widget):
    """Set stylesheet.

    Args:
        widget (QtWidgets.QWidget): Widget to apply stylesheet to.
    """

    this_dir = os.path.dirname(__file__)
    styles = os.path.join(this_dir, "../", "styles", "styles.qss")
    styles = os.path.normpath(styles)

    if os.path.isfile(styles):
        with open(styles) as file_:
            widget.setStyleSheet(file_.read())


def get_settings_dir():
    """Get settings directory. If it does not exist create it.

    Returns:
        str: Absolute path of knob settings directory.
    """

    user_home = os.path.expanduser("~")
    settings_dir = os.path.join(user_home, ".nuke", "default")
    # settings_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings")

    if not os.path.isdir(settings_dir):
        os.makedirs(settings_dir)
    return settings_dir


def get_settings_xml():
    """Get settings xml. If it does not exist create it.

    Returns:
        str: Absolute path of knob settings xml.
    """

    settings_xml = os.path.join(get_settings_dir(), "settings.xml")

    if not os.path.isfile(settings_xml):
        with open(settings_xml, "w") as xml:
            xml.write(templates.SETTINGS.strip())

    check_xml_well_formed(settings_xml, "settings")

    return settings_xml


def check_xml_well_formed(xml, which):
    """Check if xml is well formed, if not ask to delete it and create a new
    one.

    Args:
        xml (str): Absolute path of xml to check.
        which (str): Name of xml to process.
    """

    try:
        with open(xml, "r") as xml_file:
            ElementTree.fromstring(xml_file.read())
    except ElementTree.ParseError:
        message = "The default {} file seems to be broken. Do you want to " \
                  "reset it now?".format(which)

        reset_xml = ask_dialog(message, process_button_text="reset")
        if reset_xml:
            if os.path.isfile(xml):
                os.remove(xml)
                if which == "settings":
                    get_settings_xml()
                elif which == "current knobDefaults":
                    get_current_knob_defaults_xml()


def ask_dialog(message, process_button_text="", color_process="blue",
               cancel_button_text="cancel"):
    """Create and show ask dialog.

    Args:
        message (str): Message to display.
        process_button_text (str): Label of process button.
        color_process (str): Color of process button in the format:
            "r,g,b,a"; if set to "actionButton" then this button will become a
            blue button like all actionButton QPushWidgets.
        cancel_button_text (str): Label of reject button.

    Returns:
        Bool: True if clicked process button, otherwise False.
    """

    msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,
                                    "QMessageBox.warning()", message,
                                    QtWidgets.QMessageBox.NoButton, None)
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setObjectName("msgBox")
    msg_box.raise_()
    process_button = msg_box.addButton(process_button_text,
                                       QtWidgets.QMessageBox.AcceptRole)
    if color_process != "":
        if color_process == "blue":
            color_process = "51, 204, 255, 100"

        style = "QPushButton {background-color: rgba(%s)}" % color_process
        process_button.setStyleSheet(style)
    process_button.clearFocus()
    msg_box.setFocus()
    msg_box.addButton(cancel_button_text, QtWidgets.QMessageBox.RejectRole)
    return msg_box.exec_() == QtWidgets.QMessageBox.AcceptRole


def get_current_knob_defaults_xml():
    """Get knob defaults xml. If it does not exist create it.

    Returns:
        str: Absolute path of knob defaults xml.
    """

    # Load presets dir.
    settings_xml = get_settings_xml()
    knob_defaults_tree = ElementTree.parse(settings_xml)
    settings_root = knob_defaults_tree.getroot()

    presets_dir = ""
    cur_preset = ""

    for child in settings_root.findall("set"):
        if child.get("name") == "presets_path":
            presets_dir = child.text
        if child.get("name") == "cur_preset":
            cur_preset = child.text

    cur_knob_defaults_xml = "{}/{}".format(presets_dir, cur_preset)

    if not os.path.isdir(os.path.dirname(cur_knob_defaults_xml)):
        os.makedirs(os.path.dirname(cur_knob_defaults_xml))

    if not os.path.isfile(cur_knob_defaults_xml):
        with open(cur_knob_defaults_xml, "w") as xml:
            xml.write(templates.KNOB_DEFAULTS.strip())

    check_xml_well_formed(cur_knob_defaults_xml, "current knobDefaults")

    return cur_knob_defaults_xml


def get_root_current_xml():
    """Get root directory of current knob defaults xml.

    Returns:
        str: Absolute path of directory of current knob defaults xml.
    """

    return os.path.dirname(get_current_knob_defaults_xml())


def list_presets():
    """Get list of all presets of the current preset_dir.

    Returns:
        list: Names of all presets.
    """

    preset_dir = os.path.dirname(get_current_knob_defaults_xml())
    preset_list_all = os.listdir(preset_dir)
    preset_list = [os.path.splitext(p)[0] for p in preset_list_all if
                   os.path.splitext(p)[1] == ".xml"]

    return preset_list


def prettyprint(elem, level=0):
    """Pretty print xml.

    Args:
        elem (str): Element to process.
        level (int): Indentation level.
    """

    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            prettyprint(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def write_xml(xml, root, tree):
    """Pretyy print and write xml.

    Returns:
        Bool: True if successfully written to xml, otherwise False.
    """

    try:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)
        return True
    except:
        return False


def get_exclude_list():
    """Get all knobs that should not be listed in the knob list because it
    doesn't make sense to set a knobDefault on them.

    Returns:
        list: Names of knobs to exclude.
    """

    return ["xpos", "ypos", "name"]


def close_(window):
    """Ask to restart nuke when loading changes were applied."""

    window.close()
    if window.current_knobdefault_changed:
        # ask to restart nuke
        msg = "You need to restart Nuke before the knobDefaults changes " \
              "apply. Do you like to restart Nuke now?"
        if nuke.ask(msg):
            nuke.scriptClose()


def load_knob_defaults(init=False):
    """Read knob defaults xml and set knob defaults. Create list of KnobDefault
    objects of all knobDefaults in xml.

    Args:
        init (Bool): If True initialize the knob defualts on startup.

    Returns:
        list: All knobDefaults.
    """

    knob_default_xml = get_current_knob_defaults_xml()
    knob_defaults_tree = ElementTree.parse(knob_default_xml)
    knob_defaults_root = knob_defaults_tree.getroot()

    knob_defaults_list = []

    for child in knob_defaults_root.findall("default"):
        if not child.text or not child.get("node") or not child.get("knob"):
            continue

        # Format.
        value = child.text
        value = value.replace("&lt;", "<")
        value = value.replace("&gt;", ">")

        # Initialize the knob defaults on startup.
        if init:
            nuke.knobDefault("{}.{}".format(child.get("node"),
                                            child.get("knob")), value)

        knob_defaults_list.append(KnobDefault(child.get("node"),
                                              child.get("knob"), value))

    return knob_defaults_list


def update_knob_defaults_xml(node, knob, value, mode):
    """Delete or append knob default in knob defualts xml depending on given
    mode.

    Args:
        node (str): Name of node.
        knob (str): Name of knob.
        value (str): New knobDefault value.
        mode (str): Mode to execute ("delete" from or "append" to xml.
    """

    knob_default_xml = get_current_knob_defaults_xml()
    knob_defaults_tree = ElementTree.parse(knob_default_xml)
    knob_defaults_root = knob_defaults_tree.getroot()

    try:
        value = value.replace("<", "&lt;")
        value = value.replace(">", "&gt;")
    except AttributeError:
        pass

    if mode == "del":
        for child in knob_defaults_root.findall("default"):
            if child.get("node") == node and child.get("knob") == knob:
                knob_defaults_root.remove(child)

    if mode == "append":
        # Check if child exists.
        # If exists then update xml, if not append child.
        exists = 0

        for child in knob_defaults_root.findall("default"):
            if child.get("node") == node and child.get("knob") == knob:
                child.text = value
                exists += 1

        # Not found, append the child to xml.
        if exists == 0:
            new_default = ElementTree.Element("default")
            new_default.set("node", node)
            new_default.set("knob", knob)
            new_default.text = str(value)
            knob_defaults_root.append(new_default)

    # Update xml.
    prettyprint(knob_defaults_root)
    write_xml(knob_default_xml, knob_defaults_root, knob_defaults_tree)


def center(widget):
    """Center given window.

    Args:
        widget (QWidgets.QWidget): Widget to center.
    """

    frame_geo = widget.frameGeometry()
    widget_center = QtWidgets.QDesktopWidget().availableGeometry().center()
    frame_geo.moveCenter(widget_center)
    widget.move(frame_geo.topLeft())


class KnobDefault(object):
    """Container that holds knob default information."""

    def __init__(self, node, knob, value):
        """Initialize the KnobDefault instance.

        Args:
            node (str): Name of node.
            knob (str): Name of knob.
            value (str): Value to store.
        """

        self.node = node
        self.knob = knob
        self.value = value

    def get_node(self):
        """Get node value.

        Returns:
            str: Name of node.
        """

        return self.node

    def set_node(self, node):
        """Set node value.

        Args:
            node (str): New name of node.
        """

        self.node = node

    def get_knob(self):
        """Get knob value.

        Returns:
            str: Name of knob.
        """

        return self.knob

    def get_value(self):
        """Get current value.

        Returns:
            str: Current Value.
        """

        return self.value


def get_all_nodes():
    """Get all nodes from all node menus.

    Returns:
        list: Names of all nodes in all node menus.
    """

    all_nodes = []
    for category in nuke.menu("Nodes").items():
        for node in nuke.menu("Nodes").findItem(str(category.name())).items():
            all_nodes.append(node.name())

    return all_nodes
