#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Render missing frames
#
#----------------------------------------------------------------------------------------------------------

import os
import nuke
from PySide2.QtWidgets import (QWidget, QLineEdit, QPushButton, QApplication,
        QLayout, QGridLayout, QLabel, QHBoxLayout, QVBoxLayout, QDesktopWidget)
from PySide2.QtGui import QRegExpValidator
from PySide2.QtCore import Qt, QRegExp

class RenderMissingFrames(QWidget):
    def __init__(self):
        super(RenderMissingFrames, self).__init__()

        self.node = nuke.selectedNode()
        self.node.selectOnly()

        if self.node.Class() == 'Write':
            self.setUI()
            self.setSizePositon()
            self.show()

            # set focus
            self.checkingButton.setFocus()

    def setUI(self):
            validator = QRegExpValidator(QRegExp(r'\d*'))

            # widgets
            self.nodeLabel = QLabel(self.node.name())

            self.rangeLabel = QLabel('Frame range')
            self.rangeLabel.setAlignment(Qt.AlignRight)

            self.startText = QLineEdit()
            self.startText.setPlaceholderText('check start frame')
            self.startText.setText(str(int(nuke.root()['first_frame'].getValue())))
            self.startText.setValidator(validator)
            self.startText.editingFinished.connect(self.correct)

            self.toLabel = QLabel('-')

            self.endText = QLineEdit()
            self.endText.setPlaceholderText('check end frame')
            self.endText.setText(str(int(nuke.root()['last_frame'].getValue())))
            self.endText.setValidator(validator)
            self.endText.editingFinished.connect(self.correct)

            button_style = '''
                            QPushButton {
                                border: 1px solid;
                                border-color: #1F1F1F;
                                border-radius: 6px;
                                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #555555, stop:1 #464646);
                                padding: 4px;
                                padding-right: 13px;
                                padding-left: 13px;
                                }

                            QPushButton:hover {
                                border-color: #0099FF;
                                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #0099FF, stop:1 #007ACC);
                                color: #FFFFFF;
                                }

                            QPushButton:pressed {
                                border-color: #004C7F;
                                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #004C7F, stop:1 #003D66);
                                }
                            '''

            self.checkingButton = QPushButton('Checking')
            self.checkingButton.setStyleSheet(button_style)
            self.checkingButton.clicked.connect(self.checking)

            self.mfLabel = QLabel('Missing Frames')
            self.mfLabel.setEnabled(False)
            self.mfLabel.setAlignment(Qt.AlignRight)

            self.mfText = QLineEdit()
            self.mfText.setAlignment(Qt.AlignLeft)
            self.mfText.setReadOnly(True)
            self.mfText.setEnabled(False)
            
            self.renderButton = QPushButton('Render')
            self.renderButton.setEnabled(False)
            self.renderButton.setStyleSheet(button_style)
            self.renderButton.clicked.connect(self.renderMissingFrames)

            # set layout
            grid = QGridLayout()
            grid.setSpacing(10)
            grid.setMargin(20)

            grid.addWidget(self.nodeLabel, 0, 0)

            grid.addWidget(self.rangeLabel, 1, 1)
            grid.addWidget(self.startText, 1, 2)
            grid.addWidget(self.toLabel, 1, 3)
            grid.addWidget(self.endText, 1, 4)
            grid.addWidget(self.checkingButton, 1, 5)
            
            grid.addWidget(self.mfLabel, 2, 1)
            grid.addWidget(self.mfText, 2, 2, 1, 4)

            grid.addWidget(self.renderButton, 3, 1, 1, 5, Qt.AlignBottom)
            grid.setRowMinimumHeight(3, 40)

            grid.addWidget(QLabel(''), 0, 6)

            grid.setColumnMinimumWidth(0, 20)
            grid.setColumnMinimumWidth(6, 20)

            self.setLayout(grid)

    def setSizePositon(self):
        self.setWindowTitle('Render Missing Frames')
        self.resize(600, 200)

        # center
        qr = self.frameGeometry()
        screenCenter = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(screenCenter)
        self.move(qr.topLeft())
        
        # pin top
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def correct(self):
        try:
            self.sender().setText(str(int(self.sender().text())))
        except:
            pass

    # find missing frames
    def missingFrames(self):
        frameNum = self.node['file'].getValue().split('.')[-2]
        
        if frameNum.startswith('%'):
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

    # when clicked checking button
    def checking(self):
        try:
            self.start = int(self.startText.text())
            self.end = int(self.endText.text())
        except:
            self.mfLabel.setText('Missing Frames')
            self.mfLabel.setEnabled(False)
            self.mfText.setEnabled(False)
            self.mfText.setText('')
            self.renderButton.setEnabled(False)
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
            else:
                self.mfLabel.setText('Missing Frames')
                self.mfLabel.setEnabled(False)
                self.mfText.setEnabled(False)
                self.mfText.setText('')
                self.renderButton.setEnabled(False)

    # render
    def renderMissingFrames(self):
        self.close()
        frameRanges = nuke.FrameRanges(self.frames)
        nuke.execute(self.node, frameRanges)

    # event
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.checking()
        elif event.key() == Qt.Key_Escape:
            self.close()

rmf = RenderMissingFrames()
rmf.checking()