#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set to frame
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    node['output.first_lock'].setValue(True)
    node['output.first'].setValue(nuke.frame())