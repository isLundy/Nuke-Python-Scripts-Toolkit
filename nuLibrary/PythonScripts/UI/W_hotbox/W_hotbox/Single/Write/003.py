#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Evaluation file path
#
#----------------------------------------------------------------------------------------------------------

eval = nuke.selectedNode().knob('file').evaluate()
nuke.selectedNode().knob('file').setValue(eval)