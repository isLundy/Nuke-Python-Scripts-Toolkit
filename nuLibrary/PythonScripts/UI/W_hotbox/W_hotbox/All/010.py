#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Clear Animated
# COLOR: #7f0000
#
#----------------------------------------------------------------------------------------------------------

for c in nuke.selectedNodes():
    for a,b in c.knobs().items():
        if b.isAnimated():   
            b.clearAnimated()