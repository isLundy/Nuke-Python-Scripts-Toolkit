#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Custom Size 2
#
#----------------------------------------------------------------------------------------------------------

import nuke
import nukescripts

class BackdropCustomSize(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'Custom Size')
        self.bd = nuke.selectedNode()
        self.bdw = int(self.bd['bdwidth'].getValue())
        self.bdh = int(self.bd['bdheight'].getValue())

        self.width = nuke.Int_Knob('width', '<b>Width')
        self.width.setValue(self.bdw)
        self.spacer1 = nuke.Text_Knob('spacer1', '', ' ')
        self.height = nuke.Int_Knob('height', ' <b>Height')
        self.height.setValue(self.bdh)
        self.spacer2 = nuke.Text_Knob('spacer2', '', ' ')
        self.tooltip = nuke.Text_Knob('tooltip', '<b>Tip:', "<font color='#FCB434'>Defaults to current size.<font>")
        self.spacer3 = nuke.Text_Knob('spacer1', '', ' ')

        for k in (self.width, self.spacer1, self.height, self.spacer2, self.tooltip, self.spacer3):
            self.addKnob(k)

    def excute(self):
        self.bd['bdwidth'].setValue(float(self.width.value()))
        self.bd['bdheight'].setValue(float(self.height.value()))

bd = BackdropCustomSize()
bd.showModalDialog()
bd.excute()