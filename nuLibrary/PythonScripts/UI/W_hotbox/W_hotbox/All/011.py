#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Backdrop Size
#
#----------------------------------------------------------------------------------------------------------

i = nuke.selectedNodes()

bdlist = []
otherlist = []

for node in i:
    if node.Class() == 'BackdropNode':
        bdlist.append(node)
    else:
        otherlist.append(node)

for node in otherlist:
    node['selected'].setValue(False)

try:
    bdwidth = int(bdlist[0]['bdwidth'].getValue())
    bdheight = int(bdlist[0]['bdheight'].getValue())
except:
    pass
else:
    bd = nuke.Panel("Backdrop Size")
    bd.addBooleanCheckBox("<p><font color='#FCB434'>Defalut to current size if only one node is selected,<br><br>otherwise the last selected one.</font></p>", True)
    bd.addSingleLineInput('Width', bdwidth)
    bd.addSingleLineInput('Height', bdheight)
    bd.setWidth(420)
    result = bd.show()

    if result == True:
        bdw = float(bd.value('Width'))
        bdh = float(bd.value('Height'))

        if int(bdw) >= 40 and int(bdh) >= 20:
            for node in bdlist:
                node['bdwidth'].setValue(bdw)
                node['bdheight'].setValue(bdh)