#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Sort nodes
#
#----------------------------------------------------------------------------------------------------------

xpos = []
ypos = []
nodes = nuke.selectedNodes()
for node in nodes:
    xpos.append(node.xpos())
    ypos.append(node.ypos())

xp = min(xpos)
yp = min(ypos)
n = 0
for node in sorted(nodes, key=lambda x:x['file'].getValue().split('/')[-1]):
    node.setXYpos(xp+200*n, yp)
    n += 1