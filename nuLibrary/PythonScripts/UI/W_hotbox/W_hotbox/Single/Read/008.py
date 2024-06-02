#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Raw
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    if int(node['raw'].getValue()) == 0:
        node['raw'].setValue(1)
    else:
        node['raw'].setValue(0)