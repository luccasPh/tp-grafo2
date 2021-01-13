# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\config.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, QtCore, QtGui
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


class Config(object):
    def setupUi(self, Form, cava, casa):
        self.image = os.path.join(os.path.dirname(__file__), "image")
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(371, 566)
        Form.setStyleSheet(_fromUtf8(""))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 161, 331))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(70, 290, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 51, 51))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(
            QtGui.QPixmap(_fromUtf8(os.path.join(self.image, "hyoga.png")))
        )
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(
            QtGui.QPixmap(_fromUtf8(os.path.join(self.image, "seya2.png")))
        )
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(70, 140, 62, 22))
        self.doubleSpinBox_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.doubleSpinBox_3.setDecimals(1)
        self.doubleSpinBox_3.setMinimum(1.0)
        self.doubleSpinBox_3.setMaximum(5.0)
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(70, 200, 62, 22))
        self.doubleSpinBox_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_4.setDecimals(1)
        self.doubleSpinBox_4.setMinimum(1.0)
        self.doubleSpinBox_4.setMaximum(5.0)
        self.doubleSpinBox_4.setSingleStep(0.1)
        self.doubleSpinBox_4.setProperty("value", 1.2)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(70, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(70, 170, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(70, 260, 62, 22))
        self.doubleSpinBox_5.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_5.setDecimals(1)
        self.doubleSpinBox_5.setMinimum(1.0)
        self.doubleSpinBox_5.setMaximum(5.0)
        self.doubleSpinBox_5.setSingleStep(0.1)
        self.doubleSpinBox_5.setProperty("value", 1.1)
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(70, 80, 62, 22))
        self.doubleSpinBox_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setMinimum(1.0)
        self.doubleSpinBox_2.setMaximum(5.0)
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 51, 51))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(
            QtGui.QPixmap(_fromUtf8(os.path.join(self.image, "shiryu.png")))
        )
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 260, 51, 61))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(
            QtGui.QPixmap(_fromUtf8(os.path.join(self.image, "ikki.png")))
        )
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(70, 20, 62, 22))
        self.doubleSpinBox.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(1.0)
        self.doubleSpinBox.setMaximum(5.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 51, 51))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(
            QtGui.QPixmap(_fromUtf8(os.path.join(self.image, "shun.png")))
        )
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(70, 230, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(70, 45, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 50, 181, 501))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_9.setGeometry(QtCore.QRect(110, 60, 62, 22))
        self.doubleSpinBox_9.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_9.setDecimals(0)
        self.doubleSpinBox_9.setMinimum(50.0)
        self.doubleSpinBox_9.setMaximum(250.0)
        self.doubleSpinBox_9.setSingleStep(5.0)
        self.doubleSpinBox_9.setProperty("value", 55.0)
        self.doubleSpinBox_9.setObjectName(_fromUtf8("doubleSpinBox_9"))
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_10.setGeometry(QtCore.QRect(110, 20, 62, 22))
        self.doubleSpinBox_10.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_10.setDecimals(0)
        self.doubleSpinBox_10.setMinimum(50.0)
        self.doubleSpinBox_10.setMaximum(250.0)
        self.doubleSpinBox_10.setSingleStep(5.0)
        self.doubleSpinBox_10.setObjectName(_fromUtf8("doubleSpinBox_10"))
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(10, 10, 91, 41))
        self.label_20.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(_fromUtf8(""))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(10, 50, 91, 41))
        self.label_21.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(_fromUtf8(""))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_11.setGeometry(QtCore.QRect(110, 140, 62, 22))
        self.doubleSpinBox_11.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_11.setDecimals(0)
        self.doubleSpinBox_11.setMinimum(50.0)
        self.doubleSpinBox_11.setMaximum(250.0)
        self.doubleSpinBox_11.setSingleStep(5.0)
        self.doubleSpinBox_11.setProperty("value", 70.0)
        self.doubleSpinBox_11.setObjectName(_fromUtf8("doubleSpinBox_11"))
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_12.setGeometry(QtCore.QRect(110, 100, 62, 22))
        self.doubleSpinBox_12.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_12.setDecimals(0)
        self.doubleSpinBox_12.setMinimum(50.0)
        self.doubleSpinBox_12.setMaximum(250.0)
        self.doubleSpinBox_12.setSingleStep(5.0)
        self.doubleSpinBox_12.setProperty("value", 60.0)
        self.doubleSpinBox_12.setObjectName(_fromUtf8("doubleSpinBox_12"))
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(10, 130, 91, 41))
        self.label_22.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(_fromUtf8(""))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(10, 90, 91, 41))
        self.label_23.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(_fromUtf8(""))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.doubleSpinBox_17 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_17.setGeometry(QtCore.QRect(110, 220, 62, 22))
        self.doubleSpinBox_17.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_17.setDecimals(0)
        self.doubleSpinBox_17.setMinimum(50.0)
        self.doubleSpinBox_17.setMaximum(250.0)
        self.doubleSpinBox_17.setSingleStep(5.0)
        self.doubleSpinBox_17.setProperty("value", 80.0)
        self.doubleSpinBox_17.setObjectName(_fromUtf8("doubleSpinBox_17"))
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(10, 290, 91, 41))
        self.label_28.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(_fromUtf8(""))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.doubleSpinBox_18 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_18.setGeometry(QtCore.QRect(110, 180, 62, 22))
        self.doubleSpinBox_18.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_18.setDecimals(0)
        self.doubleSpinBox_18.setMinimum(50.0)
        self.doubleSpinBox_18.setMaximum(250.0)
        self.doubleSpinBox_18.setSingleStep(5.0)
        self.doubleSpinBox_18.setProperty("value", 75.0)
        self.doubleSpinBox_18.setObjectName(_fromUtf8("doubleSpinBox_18"))
        self.doubleSpinBox_19 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_19.setGeometry(QtCore.QRect(110, 260, 62, 22))
        self.doubleSpinBox_19.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_19.setDecimals(0)
        self.doubleSpinBox_19.setMinimum(50.0)
        self.doubleSpinBox_19.setMaximum(250.0)
        self.doubleSpinBox_19.setSingleStep(5.0)
        self.doubleSpinBox_19.setProperty("value", 85.0)
        self.doubleSpinBox_19.setObjectName(_fromUtf8("doubleSpinBox_19"))
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(10, 210, 91, 41))
        self.label_29.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(_fromUtf8(""))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.doubleSpinBox_20 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_20.setGeometry(QtCore.QRect(110, 300, 62, 22))
        self.doubleSpinBox_20.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_20.setDecimals(0)
        self.doubleSpinBox_20.setMinimum(50.0)
        self.doubleSpinBox_20.setMaximum(250.0)
        self.doubleSpinBox_20.setSingleStep(5.0)
        self.doubleSpinBox_20.setProperty("value", 90.0)
        self.doubleSpinBox_20.setObjectName(_fromUtf8("doubleSpinBox_20"))
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setGeometry(QtCore.QRect(10, 170, 91, 41))
        self.label_30.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(_fromUtf8(""))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        self.label_31.setGeometry(QtCore.QRect(10, 250, 91, 41))
        self.label_31.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(_fromUtf8(""))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.doubleSpinBox_21 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_21.setGeometry(QtCore.QRect(110, 380, 62, 22))
        self.doubleSpinBox_21.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_21.setDecimals(0)
        self.doubleSpinBox_21.setMinimum(50.0)
        self.doubleSpinBox_21.setMaximum(250.0)
        self.doubleSpinBox_21.setSingleStep(5.0)
        self.doubleSpinBox_21.setProperty("value", 100.0)
        self.doubleSpinBox_21.setObjectName(_fromUtf8("doubleSpinBox_21"))
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        self.label_32.setGeometry(QtCore.QRect(10, 450, 91, 41))
        self.label_32.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(_fromUtf8(""))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.doubleSpinBox_22 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_22.setGeometry(QtCore.QRect(110, 340, 62, 22))
        self.doubleSpinBox_22.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_22.setDecimals(0)
        self.doubleSpinBox_22.setMinimum(50.0)
        self.doubleSpinBox_22.setMaximum(250.0)
        self.doubleSpinBox_22.setSingleStep(5.0)
        self.doubleSpinBox_22.setProperty("value", 95.0)
        self.doubleSpinBox_22.setObjectName(_fromUtf8("doubleSpinBox_22"))
        self.doubleSpinBox_23 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_23.setGeometry(QtCore.QRect(110, 420, 62, 22))
        self.doubleSpinBox_23.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_23.setDecimals(0)
        self.doubleSpinBox_23.setMinimum(50.0)
        self.doubleSpinBox_23.setMaximum(250.0)
        self.doubleSpinBox_23.setSingleStep(5.0)
        self.doubleSpinBox_23.setProperty("value", 110.0)
        self.doubleSpinBox_23.setObjectName(_fromUtf8("doubleSpinBox_23"))
        self.label_33 = QtWidgets.QLabel(self.groupBox_2)
        self.label_33.setGeometry(QtCore.QRect(10, 370, 101, 41))
        self.label_33.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(_fromUtf8(""))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.doubleSpinBox_24 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_24.setGeometry(QtCore.QRect(110, 460, 62, 22))
        self.doubleSpinBox_24.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);;"))
        self.doubleSpinBox_24.setDecimals(0)
        self.doubleSpinBox_24.setMinimum(50.0)
        self.doubleSpinBox_24.setMaximum(250.0)
        self.doubleSpinBox_24.setSingleStep(5.0)
        self.doubleSpinBox_24.setProperty("value", 120.0)
        self.doubleSpinBox_24.setObjectName(_fromUtf8("doubleSpinBox_24"))
        self.label_34 = QtWidgets.QLabel(self.groupBox_2)
        self.label_34.setGeometry(QtCore.QRect(10, 330, 91, 41))
        self.label_34.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(_fromUtf8(""))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtWidgets.QLabel(self.groupBox_2)
        self.label_35.setGeometry(QtCore.QRect(10, 410, 91, 41))
        self.label_35.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(_fromUtf8(""))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 371, 591))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setPixmap(
            QtGui.QPixmap(_fromUtf8(os.path.join(self.image, "fundo.jpg")))
        )
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 520, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            _fromUtf8(
                "border-style: outset;\n"
                "border-width: 2px;\n"
                "border-radius: 15px;\n"
                "border-color: rgb(255, 0, 0);\n"
                "padding: 4px;\n"
                "background-color: red;"
            )
        )
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.default)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 520, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            _fromUtf8(
                "border-style: outset;\n"
                "border-width: 2px;\n"
                "border-radius: 15px;\n"
                "border-color: rgb(190, 190, 190);\n"
                "padding: 4px;\n"
                "background-color: green"
            )
        )
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(lambda: self.salvar(Form, cava, casa))

        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(70, 0, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sitka Small"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_11.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.doubleSpinBox.setProperty("value", 1.5)
        self.doubleSpinBox_2.setProperty("value", 1.4)
        self.doubleSpinBox_3.setProperty("value", 1.3)

    def default(self):
        self.doubleSpinBox.setProperty("value", 1.5)
        self.doubleSpinBox_2.setProperty("value", 1.4)
        self.doubleSpinBox_3.setProperty("value", 1.3)
        self.doubleSpinBox_4.setProperty("value", 1.2)
        self.doubleSpinBox_5.setProperty("value", 1.1)
        self.doubleSpinBox_9.setProperty("value", 55.0)
        self.doubleSpinBox_10.setProperty("value", 50)
        self.doubleSpinBox_11.setProperty("value", 70.0)
        self.doubleSpinBox_12.setProperty("value", 60.0)
        self.doubleSpinBox_17.setProperty("value", 80.0)
        self.doubleSpinBox_18.setProperty("value", 75.0)
        self.doubleSpinBox_19.setProperty("value", 85.0)
        self.doubleSpinBox_20.setProperty("value", 90.0)
        self.doubleSpinBox_21.setProperty("value", 100.0)
        self.doubleSpinBox_22.setProperty("value", 95.0)
        self.doubleSpinBox_23.setProperty("value", 110.0)
        self.doubleSpinBox_24.setProperty("value", 120.0)

    def salvar(self, Form, cava, casa):
        cava[0].poder = self.doubleSpinBox.value()
        cava[1].poder = self.doubleSpinBox_2.value()
        cava[2].poder = self.doubleSpinBox_3.value()
        cava[3].poder = self.doubleSpinBox_4.value()
        cava[4].poder = self.doubleSpinBox_5.value()

        casa[1].difi = self.doubleSpinBox_9.value()
        casa[0].difi = self.doubleSpinBox_10.value()
        casa[3].difi = self.doubleSpinBox_11.value()
        casa[2].difi = self.doubleSpinBox_12.value()
        casa[5].difi = self.doubleSpinBox_17.value()
        casa[4].difi = self.doubleSpinBox_18.value()
        casa[6].difi = self.doubleSpinBox_19.value()
        casa[7].difi = self.doubleSpinBox_20.value()
        casa[9].difi = self.doubleSpinBox_21.value()
        casa[8].difi = self.doubleSpinBox_22.value()
        casa[10].difi = self.doubleSpinBox_23.value()
        casa[11].difi = self.doubleSpinBox_24.value()

        Form.close()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Cavaleiros Poder", None))
        self.label_10.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" color:#ff007f;">Ikki</span></p></body></html>',
                None,
            )
        )
        self.label_6.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" color:#00caca;">Shiryu</span></p></body></html>',
                None,
            )
        )
        self.label_7.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" color:#aaffff;">Hyoga</span></p></body></html>',
                None,
            )
        )
        self.label_8.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" color:#bd008e;">Shun</span></p></body></html>',
                None,
            )
        )
        self.label_5.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" color:#ff0000;">Seya</span></p></body></html>',
                None,
            )
        )
        self.groupBox_2.setTitle(_translate("Form", "Casas Dificuldades", None))
        self.label_20.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:18pt; color:#ffff00;">ÁRIES</span></p></body></html>',
                None,
            )
        )
        self.label_21.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:16pt; color:#ffff00;">TOURO</span></p></body></html>',
                None,
            )
        )
        self.label_22.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:14pt; color:#ffff00;">CÂNCER</span></p></body></html>',
                None,
            )
        )
        self.label_23.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:14pt; color:#ffff00;">GÊMEOS</span></p></body></html>',
                None,
            )
        )
        self.label_28.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" color:#ffff00;">ESCORPIÃO</span></p></body></html>',
                None,
            )
        )
        self.label_29.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:14pt; color:#ffff00;">VIRGEM</span></p></body></html>',
                None,
            )
        )
        self.label_30.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:18pt; color:#ffff00;">LEÃO</span></p></body></html>',
                None,
            )
        )
        self.label_31.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:16pt; color:#ffff00;">LIBRAS</span></p></body></html>',
                None,
            )
        )
        self.label_32.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:18pt; color:#ffff00;">PEIXE</span></p></body></html>',
                None,
            )
        )
        self.label_33.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:9pt; color:#ffff00;">CAPRICÓRNIO</span></p></body></html>',
                None,
            )
        )
        self.label_34.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" color:#ffff00;">SARGITÁRIO</span></p></body></html>',
                None,
            )
        )
        self.label_35.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ffff00;">AQUÁRIOS</span></p></body></html>',
                None,
            )
        )
        self.pushButton.setText(_translate("Form", "DEFAULT", None))
        self.pushButton_2.setText(_translate("Form", "SALVAR", None))
        self.label_11.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:20pt; color:#0000ff;">CONFIGURAÇÃO</span></p></body></html>',
                None,
            )
        )
