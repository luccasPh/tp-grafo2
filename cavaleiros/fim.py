# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\fim.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import QtMultimedia
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Fim(object):
    def setupUi(self, Form):
        audio = os.path.join(os.path.dirname(__file__), 'audio')
        self.image = os.path.join(os.path.dirname(__file__), 'image')
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(570, 428)
        Form.setStyleSheet(_fromUtf8(""))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 571, 431))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(self.image, 'fim.jpg'))))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 151, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        audioUrl = QtCore.QUrl.fromLocalFile(os.path.join(audio, 'fim.mp3'))
        audioOutput = QtMultimedia.QMediaContent(audioUrl)
        self.mediaObject = QtMultimedia.QMediaPlayer()
        self.mediaObject.setMedia(audioOutput)
        self.mediaObject.play()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:48pt; color:#ffff00;\">FIM</span></p></body></html>", None))

"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
"""

