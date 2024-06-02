#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Center
#
#----------------------------------------------------------------------------------------------------------

width = nuke.root()['format'].value().width()
height = nuke.root()['format'].value().height()
center = (width/2, height/2)

for node in nuke.selectedNodes():
    node['translate'].setValue(center)