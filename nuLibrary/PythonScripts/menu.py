'''
# Author: Lundy Hu
# Email: lundyhu@outlook.com
# URL: https://github.com/isLundy/Nuke-Python-Scripts-Toolkit.git
'''
import nuke
import nukescripts
import platform
from pathlib import Path



nMajor = nuke.NUKE_VERSION_MAJOR
nMinor = nuke.NUKE_VERSION_MINOR
NPST_v = 'v1.3'

#====================3D==========
import animatedSnap3D

#====================Import_Export==========
import collectFiles
import CreateOutDirs

#====================Misc==========
#Default_Knob
from default import default_main
from default import helper
from default import about

import openExploreDir
import readFromWrite

#====================NodeGraph==========
import AlignDots
import alignNodes
import MultiChannelSplit

#V!ctor
import V_PresetBackdrop
import V_PostageStampGenerator
import V_ConvertGizmosToGroups

import W_scaleTree
import W_smartAlign

#====================Render==========


#====================UI==========
import AnimationMaker
import channel_hotbox
import CloseAllProperties
import SearchReplacePanel
import W_hotbox, W_hotboxManager



#===============================================================MenuBar#s>h^i~~~
s = nuke.menu("Nuke").addMenu("PythonScripts")



#=============================================================================3D
h = s.addMenu("3D", "NPST_3D.svg")

# animatedSnap3D
i = h.addMenu("animatedSnap3D", icon="NPST_Prompt_01.svg")
i.addCommand('[ go here: Node > Snap menu > Match ... ]', '', icon="NPST_Prompt_02.svg").setEnabled(False)

try:
    m = nuke.menu('Axis').findItem('Snap')
    m.addSeparator()
    m.addCommand('Match position - ANIMATED', 'animatedSnap3D.translateThisNodeToPointsAnimated()')
    m.addCommand('Match position, orientation - ANIMATED', 'animatedSnap3D.translateRotateThisNodeToPointsAnimated()')
    m.addCommand('Match position, orientation, scale - ANIMATED', 'animatedSnap3D.translateRotateScaleThisNodeToPointsAnimated()')
except:
    pass



#==================================================================Import_Export
h = s.addMenu("Import_Export", "NPST_Import_export.svg")

#CollectFiles
i = h.addMenu("Collect_Files", icon="NPST_Import_export.svg")
i.addCommand('Collect Files', 'collectFiles.collectFiles()')
i.addCommand('Help', 'collectFiles.myBlog()')

#CreateOutDirs
i = h.addMenu("Create Out Dirs", icon="NPST_Prompt_01.svg")
i.addCommand('[ Automatically Enabled ]', '',icon="NPST_Prompt_02.svg").setEnabled(False)



#===========================================================================Misc
h = s.addMenu("Misc", "NPST_Misc.svg")

# Auto open .nk as NukeX
i = h.addMenu('Auto open .nk as NukeX', icon="NPST_Misc.svg")
reg_path = Path(__file__).absolute().parent.joinpath('Misc/Auto_open_nk_as_NukeX').as_posix()
i.addCommand('Open the folder to set ( only Windows )', 'nukescripts.start(reg_path)', icon="openExploreDir.svg")

#Default_automatic knobDefaults
i = h.addMenu("Default_automatic knobDefaults", icon="NPST_Misc.svg")
i.addCommand("Defaults window", default_main.show_defaults_window)
i.addSeparator()
i.addCommand("About", about.show_about, icon="")

nuke.menu("Animation").addCommand("Default/Set as new knobDefault",
                                  "default_main.create_default()")

nuke.menu("Animation").addCommand("Default/Show knob list",
                                  "default_main.show_knob_list()")

nuke.menu("Animation").addCommand("Default/Reset",
                                  "default_main.reset_to_default()")

helper.load_knob_defaults(init=True)

#openExploreDir
i = h.addMenu("OpenExploreDir", icon="NPST_Misc.svg")
i.addCommand("Open nk or file dir", "openExploreDir.openFileDir()", "+b", icon="openExploreDir.svg")
i.addCommand("Open .nuke dir", "openExploreDir.openDotNuke()", "+0", icon="openExploreDir.svg")
i.addCommand("Open nuke installation dir", "openExploreDir.openInstallDir()", icon="openExploreDir.svg")

#readFromWrite
h.addCommand('Read from Write', 'readFromWrite.run()', '+r', icon="NPST_Misc.svg")



#======================================================================NodeGraph
h = s.addMenu("NodeGraph", "NPST_Nodegraph.svg")

#AlignDots
h.addCommand("AlignDots", "AlignDots.AlignDots()", "#0", icon="NPST_Nodegraph.svg", shortcutContext=2)

#AlignNodes
i = h.addMenu("AlignNodes", icon="NPST_Nodegraph.svg")
i.addCommand("hCenter", "alignNodes.alignNodes( nuke.selectedNodes(), direction='x' )", "#5", icon="Align_hCenter.svg")
i.addCommand("vCenter", "alignNodes.alignNodes( nuke.selectedNodes(), direction='y' )", "^5", icon="Align_vCenter.svg")

#MultiChannelSplit
h.addCommand("MultiChannelSplit", "MultiChannelSplit.MultiChannelSplit()", "#m", icon="NPST_Nodegraph.svg")

#W_scaleTree
operatingSystem = platform.system()
if operatingSystem == "Linux":
    h.addCommand("W_scaleTree", "W_scaleTree.scaleTreeFloatingPanel()", "#1", icon="NPST_Nodegraph.svg")
else:
    h.addCommand("W_scaleTree", "W_scaleTree.scaleTreeFloatingPanel()", "#`", icon="NPST_Nodegraph.svg")

#W_smartAlign
i = h.addMenu("W_smartAlign", icon="NPST_Nodegraph.svg")
i.addCommand("Up", "W_smartAlign.alignNodes('up')", "#8", icon="Align_Top.svg", shortcutContext=2)
i.addCommand("Down", "W_smartAlign.alignNodes('down')", "#2", icon="Align_Bottom.svg", shortcutContext=2)
i.addCommand("Left", "W_smartAlign.alignNodes('left')", "#4", icon="Align_Left.svg", shortcutContext=2)
i.addCommand("Right", "W_smartAlign.alignNodes('right')", "#6", icon="Align_Right.svg", shortcutContext=2)

# V!ctor
h.addSeparator()
i = h.addMenu("V!ctor", icon="NPST_Nodegraph.svg")
i.addCommand("Convert Gizmo to Group", "V_ConvertGizmosToGroups.convertGizmosToGroups()", "^+h")
i.addCommand("Generate PostageStamp from node", "V_PostageStampGenerator.postageStampGenerator()", "#^p")
i.addCommand("Preset Backdrop", "V_PresetBackdrop.presetBackdrop()", "#^b")



#=============================================================================UI
h = s.addMenu("UI", "NPST_UI.svg")

# AnimationMaker
i = h.addMenu("AnimationMaker", icon="NPST_Prompt_01.svg")
i.addCommand("[ go here: Node > Animation (right-click) > Animation Maker... ]", '', icon="NPST_Prompt_02.svg").setEnabled(False)

#Channel hotbox
h.addCommand("Channel HotBox", "channel_hotbox.start()", "#q", icon="NPST_UI.svg")

#CloseAllProperties
h.addCommand("CloseAllProperties", "CloseAllProperties.CloseAllProperties()", "+d", icon="NPST_UI.svg")

# SearchReplacePanel
i = h.addMenu("SearchReplacePanel", icon="NPST_Prompt_01.svg")
i.addCommand("[ go here: Pane (right-click) > Windows > Custom > SearchReplace ]", '', icon="NPST_Prompt_02.svg").setEnabled(False)

# W_hotbox
i = h.addMenu("W_hotbox", icon="NPST_Prompt_01.svg")
i.addCommand("[ go here: Menu > Edit > W_hotbox ]", '', icon="NPST_Prompt_02.svg").setEnabled(False)


#===========================================================================Info
s.addSeparator()
h = s.addMenu("Info", "NPST_Info.svg")
h.addCommand("GitHub", "nukescripts.start('https://github.com/isLundy/Nuke-Python-Scripts-Toolkit.git')", icon="NPST_GitHub.svg")
h.addCommand(NPST_v, "nukescripts.start('https://github.com/isLundy/Nuke-Python-Scripts-Toolkit/releases/latest')", icon="NPST_Version.svg")



#----------------------------------------------------------#Panel(Pane)#p>e^c~~~
p = nuke.menu('Pane')

#SearchReplacePanel
def addSRPanel():
        '''Run the panel script and add it as a tab into the pane it is called from'''
        myPanel = SearchReplacePanel.SearchReplacePanel()
        return myPanel.addToPane()
        #THIS LINE WILL ADD THE NEW ENTRY TO THE PANE MENU
nuke.menu('Pane').addCommand('SearchReplace', addSRPanel)
        #THIS LINE WILL REGISTER THE PANEL SO IT CAN BE RESTORED WITH LAYOUTS
nukescripts.registerPanel('com.ohufx.SearchReplace', addSRPanel)