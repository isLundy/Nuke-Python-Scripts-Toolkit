#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Swap
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    option = node['operation']
    if int(option.getValue()) == 0:
        option.setValue(1)
    else:
        option.setValue(0)