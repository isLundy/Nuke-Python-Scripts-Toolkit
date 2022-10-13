#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Render Missing Frames
#
#----------------------------------------------------------------------------------------------------------

import os
from PySide2.QtWidgets import (QWidget, QLineEdit, QPushButton, QApplication,
                QLabel, QHBoxLayout, QVBoxLayout, QDesktopWidget)
from PySide2.QtGui import QCursor
from PySide2.QtCore import Qt

class RenderMissingFrames(QWidget):
    def __init__(self):
        super(RenderMissingFrames, self).__init__()

        self.node = nuke.selectedNode()
        self.node.selectOnly()

        if self.node.Class() == 'Write':
            self.setUI()
            self.setPZ()
            self.show()

    def setUI(self):
            self.nodeLabel = QLabel(self.node.name())

            self.rangeLabel = QLabel('Frame range')

            self.startText = QLineEdit()
            self.startText.setPlaceholderText('check start frame')
            self.startText.setText(str(int(nuke.root()['first_frame'].getValue())))

            self.toLabel = QLabel('-')

            self.endText = QLineEdit()
            self.endText.setPlaceholderText('check end frame')
            self.endText.setText(str(int(nuke.root()['last_frame'].getValue())))

            self.checkingButton = QPushButton('Checking')
            self.checkingButton.clicked.connect(self.checking)

            self.mfLabel = QLabel('Missing Frames')
            self.mfLabel.setEnabled(False)

            self.mfText = QLineEdit()
            self.mfText.setReadOnly(True)
            self.mfText.setEnabled(False)
            
            self.renderButton = QPushButton('Render Missing Frames')
            self.renderButton.setEnabled(False)
            self.renderButton.clicked.connect(self.renderMissingFrames)

            hbox = QHBoxLayout()
            hbox.addWidget(self.nodeLabel)
            hbox.addWidget(self.rangeLabel)
            hbox.addWidget(self.startText)
            hbox.addWidget(self.toLabel)
            hbox.addWidget(self.endText)
            hbox.addWidget(self.checkingButton)
            hbox.addWidget(self.mfLabel)
            hbox.addWidget(self.mfText)
            hbox.addStretch()

            vbox = QVBoxLayout()
            vbox.addStretch()
            vbox.addLayout(hbox)
            vbox.addStretch()
            vbox.addWidget(self.renderButton)

            self.setLayout(vbox)

    def setPZ(self):
        self.setWindowTitle('Render Missing Frames')
        self.resize(1200, 200)

        qr = self.frameGeometry()
        screenCenter = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(screenCenter)
        self.move(qr.topLeft())
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def missingFrames(self):
        frameNum = self.node['file'].getValue().split('.')[-2]
        evalStr = self.node['file'].evaluate().rsplit('.', 2)
        seq = '%s.%s.%s'%(evalStr[0], frameNum, evalStr[-1])

        self.frames = []
        for frame in range(self.start, self.end+1):
            file = seq%frame
            if not os.path.exists(file):
                self.frames.append(frame)

        self.missingNums = ''
        if self.frames:
            for frame in self.frames:
                if frame-1 in self.frames:
                    if frame-2 in self.frames:
                        self.missingNums = self.missingNums.replace(str(frame-1), str(frame))
                    else:
                        self.missingNums += '-%s'%frame
                else:
                    self.missingNums += ' %s'%frame

        self.missingNums = self.missingNums.strip()

    def checking(self):
        try:
            self.start = int(self.startText.text())
            self.end = int(self.endText.text())
        except:
            pass
        else:
            if self.start <= self.end:
                self.missingFrames()
                self.mfLabel.setText('Missing {} Frames'.format(len(self.frames)))

                if self.frames:
                    self.mfLabel.setEnabled(True)
                    self.mfText.setEnabled(True)
                    self.mfText.setText(self.missingNums)
                    self.renderButton.setEnabled(True)
                else:
                    self.mfLabel.setEnabled(False)
                    self.mfText.setEnabled(False)
                    self.mfText.setText('None')
                    self.renderButton.setEnabled(False)

    def renderMissingFrames(self):
        self.close()
        frameRanges = nuke.FrameRanges(self.frames)
        nuke.execute(self.node, frameRanges)

mf = RenderMissingFrames()