#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Anisotropic
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('filter').setValue('Trilinear')