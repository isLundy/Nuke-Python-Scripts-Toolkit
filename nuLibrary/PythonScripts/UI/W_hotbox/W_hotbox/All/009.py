#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Auto Crop
#
#----------------------------------------------------------------------------------------------------------

import nuke
import nukescripts

class AutoCrop(nukescripts.PythonPanel):

    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'Auto Crop')
        self.firstFrame = nuke.Int_Knob('firstFrame', 'Frame Range')
        self.firstFrame.setValue(nuke.Root().firstFrame())

        self.lastFrame = nuke.Int_Knob('lastFrame', ' ')
        self.lastFrame.setValue(nuke.Root().lastFrame())
        self.lastFrame.clearFlag(nuke.STARTLINE)

        self.inc = nuke.Int_Knob('increment', 'Increment')
        self.inc.setValue(1)

        self.channel = nuke.Enumeration_Knob('channel', 'Channel', ['rgba', 'rgb', 'r', 'g', 'b', 'a'])

        for k in (self.firstFrame, self.lastFrame, self.inc, self.channel):
            self.addKnob(k)

    def autoCrop(self):
        if self.showModalDialog():
            nukescripts.autocrop(first=self.firstFrame.value(), last=self.lastFrame.value(), inc=self.inc.value(), layer=self.channel.value())

AutoCrop().autoCrop()