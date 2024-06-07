# URL: https://github.com/isLundy/openExploreDir
# version: 1.2

import nuke
import nukescripts
from pathlib import Path

# open main
def openExplorer(path):
    nukescripts.start(path.as_posix())

# open the current project directory or the file knob directory of the selected node(like Write Node, ReadGeo Node, Camera Node, WriteGeo, etc).
def openFileDir():

    if len(nuke.selectedNodes()) != 0:
        for i in nuke.selectedNodes():
            try:
                path = Path(i.knob('file').evaluate()).parent
                openExplorer(path)
            except:
                pass

    else:
        path = Path(nuke.root().name()).parent
        if path:
            openExplorer(path)

# open .nuke directory
def openDotNuke():
    path = Path.home().joinpath('.nuke')
    openExplorer(path)

# open nuke installation directory
def openInstallDir():
    path = Path(nuke.EXE_PATH).parent
    openExplorer(path)