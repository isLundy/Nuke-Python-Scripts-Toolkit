#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Conver FilePath
#
#----------------------------------------------------------------------------------------------------------

# a = [nuke.selectedNode().knob('file').evaluate().split(".")[0]]
# b = nuke.selectedNode().knob('file').getText().split(".")[-2:]
# c = ".".join(a + b)
c = nuke.selectedNode().knob('file').evaluate()
nuke.selectedNode().knob('file').setValue(c)
