# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tela_home2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import QtMultimedia
from cavaleiros.result import Result
from cavaleiros.config import Config
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


class Cavaleiro:
    def __init__(self, poder, cava):
        self.poder = poder
        self.cava = cava
        self.vida = 5


class Casa:
    def __init__(self, x, y, d, f, t):
        self.pos_x = x
        self.pos_y = y
        self.difi = d
        self.cava_or = f
        self.title = t


class Home(object):
    def setupUi(self, Form):
        audio = os.path.join(os.path.dirname(__file__), "audio")
        self.image = os.path.join(os.path.dirname(__file__), "image")

        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(699, 380)
        self.AI = None
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 381))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(
            QtGui.QPixmap(_fromUtf8(os.path.join(self.image, "home.jpeg")))
        )

        audioUrl = QtCore.QUrl.fromLocalFile(os.path.join(audio, "abertura.mp3"))
        self.audioContent = QtMultimedia.QMediaContent(audioUrl)
        self.mediaObject = QtMultimedia.QMediaPlayer()
        self.mediaObject.setMedia(self.audioContent)
        self.mediaObject.play()

        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 50, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(
            _fromUtf8(
                "border-style: outset;\n"
                "border-width: 2px;\n"
                "border-radius: 15px;\n"
                "border-color: rgb(190, 190, 190);\n"
                "padding: 4px;\n"
                "background-color: yellow"
            )
        )
        self.pushButton_3.setIconSize(QtCore.QSize(100, 50))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(lambda: self.start_ai(Form))

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 120, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(
            _fromUtf8(
                "border-style: outset;\n"
                "border-width: 2px;\n"
                "border-radius: 15px;\n"
                "border-color: rgb(190, 190, 190);\n"
                "padding: 4px;\n"
                "background-color: rgb(0, 85, 255)"
            )
        )
        self.pushButton_4.setIconSize(QtCore.QSize(100, 50))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(lambda: self.configuracao())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.timer = QtCore.QTimer(Form)
        self.timer.timeout.connect(self.reproduzi)
        self.timer.start(201600)

        self.cavaleiros = [
            Cavaleiro(1.5, "seya3.png"),
            Cavaleiro(1.4, "shiryu2.png"),
            Cavaleiro(1.3, "hyoga2.png"),
            Cavaleiro(1.2, "shun2.png"),
            Cavaleiro(1.1, "ikki2.png"),
        ]

        self.casas = [
            Casa(37, 21, 50, "aries.png", "c1.png"),
            Casa(31, 17, 55, "touros.png", "c2.png"),
            Casa(31, 33, 60, "gemeos.png", "c3.png"),
            Casa(24, 26, 70, "cancer.png", "c4.png"),
            Casa(24, 9, 75, "leao.png", "c5.png"),
            Casa(17, 9, 80, "virgem.png", "c6.png"),
            Casa(17, 29, 85, "libras.png", "c7.png"),
            Casa(13, 37, 90, "escorpiao.png", "c8.png"),
            Casa(9, 27, 95, "sargitario.png", "c9.png"),
            Casa(9, 14, 100, "capricornio.png", "c10.png"),
            Casa(4, 13, 110, "aquarios.png", "c11.png"),
            Casa(4, 30, 120, "peixes.png", "c12.png"),
            Casa(4, 37, 0, 0, 0),
        ]

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_3.setText(_translate("Form", "PLAY", None))
        self.pushButton_4.setText(_translate("Form", "CONFIGURA", None))

    def reproduzi(self):
        self.mediaObject.setMedia(self.audioContent)
        self.mediaObject.play()

    def start_ai(self, Form):
        maxCava = sum(cava.poder for cava in self.cavaleiros) / 5
        maxCasa = sum(casa.difi for casa in self.casas) / 12
        maxTime = (maxCasa / maxCava + 34.35) // 2.5

        Form.close()
        self.timer.stop()
        self.mediaObject.stop()
        self.AI = Result(maxTime, self.cavaleiros, self.casas)

    def configuracao(self):
        self.tela = QtWidgets.QWidget()
        self.ui = Config()
        self.ui.setupUi(self.tela, self.cavaleiros, self.casas)
        self.tela.show()
