#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Remove Key
# COLOR: #7f0000
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

nodes = nuke.selectedNodes()

for node in nodes:
    for k,v in node.knobs().items():
        if v.isKey():
            v.removeKey()