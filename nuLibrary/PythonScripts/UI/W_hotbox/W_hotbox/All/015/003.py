#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Offset to Up
#
#----------------------------------------------------------------------------------------------------------

inc = 100

for node in nuke.selectedNodes():
    node.setXYpos(node.xpos(), node.ypos()-inc)