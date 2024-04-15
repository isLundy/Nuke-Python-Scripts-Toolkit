import nuke
import os

def createOutDirs():
    trgDir = os.path.dirname(nuke.filename(nuke.thisNode()))
    if not os.path.isdir(trgDir):
        os.makedirs(trgDir)

nuke.addBeforeRender(createOutDirs, nodeClass='Write')