"""This module contains the about window."""


# Import built-in modules
import webbrowser

# Import third-party modules
# pylint: disable=import-error
import nuke

try:
    from PySide2 import QtWidgets
except ImportError:
    from PySide import QtGui as QtWidgets

# Import local modules
from default import info
from default import helper


class AboutWindow(QtWidgets.QDialog):
    """About window for this tool."""

    def __init__(self):
        """Initialize the About instance."""

        super(AboutWindow, self).__init__()
        self.setWindowTitle("about default")
        self.setFixedSize(750, 500)
        self.info = info.ABOUT_INFO
        self.build_ui()

    def build_ui(self):
        """Build user interface."""

        self.create_widgets()
        self.create_layouts()
        self.create_signals()

    def create_widgets(self):
        """Create widgets."""

        self.text_info = QtWidgets.QTextEdit()
        self.text_info.setReadOnly(True)
        self.text_info.setText(self.info)
        self.push_web = QtWidgets.QPushButton("online help")
        self.push_web.setObjectName("push_blue")
        self.push_close = QtWidgets.QPushButton("close")

    def create_layouts(self):
        """Create layouts."""

        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_push = QtWidgets.QHBoxLayout()
        self.layout_push.addWidget(self.push_web)
        self.layout_push.addWidget(self.push_close)
        self.layout_main.addWidget(self.text_info)
        self.layout_main.addLayout(self.layout_push)

        self.setLayout(self.layout_main)
        helper.set_style_sheet(self)

    def create_signals(self):
        """Create signals."""

        self.push_close.clicked.connect(self.close)
        self.push_web.clicked.connect(lambda: webbrowser.open_new(
            info.WEBSITE_TOOL))


def show_about():
    """Show about panel."""

    # pylint: disable=global-variable-undefined
    # pylint: disable=invalid-name
    global about_window
    about_window = AboutWindow()
    about_window.show()
    about_window.raise_()
    helper.center(about_window)
