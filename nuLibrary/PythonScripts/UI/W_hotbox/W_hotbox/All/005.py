#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Paste to Selection
#
#----------------------------------------------------------------------------------------------------------

#===Lundy Hu===
selections = nuke.selectedNodes()
newPastedNodes = []

for selection in selections:
    selection['selected'].setValue(True)
    nuke.nodePaste('%sclipboard%')
    newPastedNodes.append(nuke.selectedNode())
    
for newPastedNode in newPastedNodes:
    newPastedNode['selected'].setValue(True)
    
#===Contributor===   
# selection = nuke.selectedNodes()
# 
# for i in selection:
    # i.knob('selected').setValue('False')
# 
# for i in selection:
    # i.knob('selected').setValue('True')
    # nuke.nodePaste('%clipboard%')
    # i.knob('selected').setValue('False')
# 
# for i in selection:
    # i.knob('selected').setValue('True')