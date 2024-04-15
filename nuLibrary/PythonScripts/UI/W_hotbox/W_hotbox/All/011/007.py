#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Custom Size
#
#----------------------------------------------------------------------------------------------------------

import nuke
import nukescripts

class BackdropCustomSize(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'Custom Size')
        self.nodes = nuke.selectedNodes("BackdropNode")

        for remove_node in nuke.selectedNodes():
            if remove_node not in self.nodes:
                remove_node.setSelected(False)

        self.bd = self.nodes[0]
        self.bdw = int(self.bd['bdwidth'].getValue())
        self.bdh = int(self.bd['bdheight'].getValue())

        self.width = nuke.Int_Knob('width', '<b>Width')
        self.width.setValue(self.bdw)
        self.spacer1 = nuke.Text_Knob('spacer1', '', ' ')
        self.height = nuke.Int_Knob('height', ' <b>Height')
        self.height.setValue(self.bdh)
        self.spacer2 = nuke.Text_Knob('spacer2', '', ' ')
        self.tooltip = nuke.Text_Knob('tooltip', '<b>Tip:', "Defaults to current size.")
        self.tooltip.setEnabled(False)
        self.spacer3 = nuke.Text_Knob('spacer1', '', ' ')

        self.excute = nuke.PyScript_Knob("excute", "Excute")
        self.excute.setFlag(nuke.STARTLINE)

        for k in (self.width, self.spacer1, self.height, self.spacer2, self.tooltip, self.spacer3, self.excute):
            self.addKnob(k)

    def zoom(self):
        for node in self.nodes:
            node['bdwidth'].setValue(float(self.width.value()))
            node['bdheight'].setValue(float(self.height.value()))

    def knobChanged(self, knob):
        if knob == self.excute:
            self.zoom()

bd = BackdropCustomSize()
bd. showModal()