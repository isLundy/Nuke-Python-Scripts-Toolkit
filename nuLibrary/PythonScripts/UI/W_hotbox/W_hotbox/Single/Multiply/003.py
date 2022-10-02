#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set Animated
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    curValue = node['value'].getValue()
    node['value'].setAnimated()
    node['value'].setValue(curValue)