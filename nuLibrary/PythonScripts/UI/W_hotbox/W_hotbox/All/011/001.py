#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Size -
#
#----------------------------------------------------------------------------------------------------------

class BackdropNode():
    def __init__(self):
        self.bdw = 100
        self.bdh = 60

        self.inc = 100

        self.nodes = nuke.selectedNodes("BackdropNode")
        for remove_node in nuke.selectedNodes():
            if remove_node not in self.nodes:
                remove_node.setSelected(False)

    def size_min(self):
        for node in self.nodes:
            if node['bdwidth'].getValue() - self.inc >= 100:
                node['bdwidth'].setValue(node['bdwidth'].getValue() - self.inc)
            if node['bdheight'].getValue() - self.inc >= 60:
                node['bdheight'].setValue(node['bdheight'].getValue() - self.inc)

    def size_max(self):
        for node in self.nodes:
            node['bdwidth'].setValue(node['bdwidth'].getValue() + self.inc)        
            node['bdheight'].setValue(node['bdheight'].getValue() + self.inc)

    def width_min(self):
        for node in self.nodes:
            if node['bdwidth'].getValue() - self.inc >= 100:
                node['bdwidth'].setValue(node['bdwidth'].getValue() - self.inc)
    
    def width_max(self):
        for node in self.nodes:
            node['bdwidth'].setValue(node['bdwidth'].getValue() + self.inc)

    def height_min(self):
        for node in self.nodes:
            if node['bdheight'].getValue() - self.inc >= 60:
                node['bdheight'].setValue(node['bdheight'].getValue() - self.inc)

    def height_max(self):
        for node in self.nodes:
            node['bdheight'].setValue(node['bdheight'].getValue() + self.inc)

bdsize = BackdropNode()
bdsize.size_min()