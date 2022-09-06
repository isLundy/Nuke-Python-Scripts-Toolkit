#"""
# ==============================================================================
# nuLibrary v9.6.2, built September 6 2022.

# Author: Lundy Hu

# Email: lundyhu@outlook.com

# See the https://github.com/isLundy/Nuke-PythonScripts-Toolkit for details.
# ==============================================================================
#"""

import sys
import os
import nuke
import nukescripts
import platform



nMajor = nuke.NUKE_VERSION_MAJOR
nMinor = nuke.NUKE_VERSION_MINOR

#--------------------------------------------------Import#
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



#==================================================Python Scripts(MenuBar and Panel)==================================================#

#----------------------------------------------------------------------------------------------------#MenuBar(Nuke)#s>h^i~~~
s = nuke.menu("Nuke").addMenu("PythonScripts")

#================================================================================3D================================================================================

# animatedSnap3D
try:
    m = nuke.menu('Axis').findItem('Snap')
    m.addSeparator()
    m.addCommand('Match position - ANIMATED', 'animatedSnap3D.translateThisNodeToPointsAnimated()')
    m.addCommand('Match position, orientation - ANIMATED', 'animatedSnap3D.translateRotateThisNodeToPointsAnimated()')
    m.addCommand('Match position, orientation, scale - ANIMATED', 'animatedSnap3D.translateRotateScaleThisNodeToPointsAnimated()')
except:
    pass

#================================================================================Import_Export================================================================================
h = s.addMenu("Import_Export", "NUPD_Import_export.svg")

#CollectFiles
i = h.addMenu("Collect_Files", icon="NUPD_Import_export.svg")
i.addCommand('Collect Files', 'collectFiles.collectFiles()')
i.addCommand('Help', 'collectFiles.myBlog()')



#================================================================================Misc================================================================================
h = s.addMenu("Misc", "NUPD_Misc.svg")

#Default_automatic knobDefaults
i = h.addMenu("Default_automatic knobDefaults", icon="NUPD_Misc.svg")
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
i = h.addMenu("OpenExploreDir", icon="NUPD_Misc.svg")
i.addCommand("Open nk or file dir", "openExploreDir.openFileDir()", "+b", icon="Lundy_Tools.png")
i.addCommand("Open .nuke dir", "openExploreDir.openDotNuke()", "+0", icon="Lundy_Tools.png")
i.addCommand("Open nuke installation dir", "openExploreDir.openExePath()", icon="Lundy_Tools.png")

#readFromWrite
h.addCommand('Read from Write', 'readFromWrite.run()', '+r', icon="NUPD_Misc.svg")



#================================================================================NodeGraph================================================================================
h = s.addMenu("NodeGraph", "NUPD_Nodegraph.svg")

#AlignDots
h.addCommand("Align Dots", "AlignDots.AlignDots()", "#0", icon="NUPD_Nodegraph.svg", shortcutContext=2)

#AlignNodes
i = h.addMenu("AlignNodes", icon="NUPD_Nodegraph.svg")
i.addCommand("hCenter", "alignNodes.alignNodes( nuke.selectedNodes(), direction='x' )", "#5", icon="Align_hCenter.svg")
i.addCommand("vCenter", "alignNodes.alignNodes( nuke.selectedNodes(), direction='y' )", "^5", icon="Align_vCenter.svg")

#MultiChannelSplit
h.addCommand("MultiChannelSplit", "MultiChannelSplit.MultiChannelSplit()", "#m", icon="NUPD_Nodegraph.svg")

#W_scaleTree
operatingSystem = platform.system()
if operatingSystem == "Linux":
    h.addCommand("W_scaleTree", "W_scaleTree.scaleTreeFloatingPanel()", "#1", icon="NUPD_Nodegraph.svg")
else:
    h.addCommand("W_scaleTree", "W_scaleTree.scaleTreeFloatingPanel()", "#`", icon="NUPD_Nodegraph.svg")

#W_smartAlign
i = h.addMenu("W_smartAlign", icon="NUPD_Nodegraph.svg")
i.addCommand("Down", "W_smartAlign.alignNodes('down')", "#2", icon="Align_Down.svg", shortcutContext=2)
i.addCommand("Left", "W_smartAlign.alignNodes('left')", "#4", icon="Align_Left.svg", shortcutContext=2)
i.addCommand("Right", "W_smartAlign.alignNodes('right')", "#6", icon="Align_Right.svg", shortcutContext=2)
i.addCommand("Up", "W_smartAlign.alignNodes('up')", "#8", icon="Align_Up.svg", shortcutContext=2)

# V!ctor
h.addSeparator()
i = h.addMenu("V!ctor", icon="NUPD_Nodegraph.svg")
i.addCommand("Convert Gizmo to Group", "V_ConvertGizmosToGroups.convertGizmosToGroups()", "^+h")
i.addCommand("Generate PostageStamp from node", "V_PostageStampGenerator.postageStampGenerator()", "#^p")
i.addCommand("Preset Backdrop", "V_PresetBackdrop.presetBackdrop()", "#^b")



#================================================================================UI================================================================================
h = s.addMenu("UI", "NUPD_UI.svg")

#Channel hotbox
h.addCommand("Channel HotBox", "channel_hotbox.start()", "#q", icon="NUPD_UI.svg")

#CloseAllProperties
h.addCommand("Close All Properties", "CloseAllProperties.CloseAllProperties()", "+d", icon="NUPD_UI.svg")

#================================================================================zLundy================================================================================






#----------------------------------------------------------------------------------------------------#Panel(Pane)#p>e^c~~~
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