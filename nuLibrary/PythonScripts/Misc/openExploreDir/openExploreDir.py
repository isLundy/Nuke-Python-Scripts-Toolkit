import nuke
import sys
import os
import platform
import subprocess

# open main
def openExplorer(path):
    operatingSystem = platform.system()

    if operatingSystem == "Windows":
        subprocess.Popen("explorer {}".format(path.replace('/', '\\')))

    elif operatingSystem == "Darwin":
        subprocess.Popen(["open", path])

    else:
        subprocess.Popen(["xdg-open", path])

# open nk or file directory
def openFileDir():

    if len(nuke.selectedNodes()) != 0:
        for i in nuke.selectedNodes():
            try:
                path = os.path.dirname(i.knob('file').evaluate())
                openExplorer(path)
            except:
                pass

    else:
        path = os.path.dirname(nuke.root().name())
        openExplorer(path)

# open .nuke directory
def openDotNuke():
    path = os.getenv('HOME') + "/.nuke"
    openExplorer(path)

# open nuke installation directory
def openExePath():
    path = os.path.dirname(nuke.EXE_PATH)
    openExplorer(path)