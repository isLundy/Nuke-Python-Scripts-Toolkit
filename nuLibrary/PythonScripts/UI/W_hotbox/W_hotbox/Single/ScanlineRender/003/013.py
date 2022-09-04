#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Bilinear
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('filter').setValue('Nearest')