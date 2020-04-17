# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color:#fff;\n"
"}")
        self.btn_mid = QtWidgets.QPushButton(Dialog)
        self.btn_mid.setGeometry(QtCore.QRect(11, 134, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mid.setFont(font)
        self.btn_mid.setStyleSheet("QPushButton{\n"
"    border:1px solid #ccc;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid #aaf;\n"
"}")
        self.btn_mid.setFlat(True)
        self.btn_mid.setObjectName("btn_mid")
        self.btn_simple = QtWidgets.QPushButton(Dialog)
        self.btn_simple.setGeometry(QtCore.QRect(11, 83, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_simple.setFont(font)
        self.btn_simple.setStyleSheet("QPushButton{\n"
"    border:1px solid #ccc;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid #aaf;\n"
"}")
        self.btn_simple.setFlat(True)
        self.btn_simple.setObjectName("btn_simple")
        self.btn_adv = QtWidgets.QPushButton(Dialog)
        self.btn_adv.setGeometry(QtCore.QRect(11, 185, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_adv.setFont(font)
        self.btn_adv.setStyleSheet("QPushButton{\n"
"    border:1px solid #ccc;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid #aaf;\n"
"}")
        self.btn_adv.setFlat(True)
        self.btn_adv.setObjectName("btn_adv")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(-10, 260, 421, 41))
        self.label_2.setStyleSheet("QLabel{\n"
"    background-color:#ccc\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "选择难度"))
        self.btn_mid.setText(_translate("Dialog", "中级(I)"))
        self.btn_simple.setText(_translate("Dialog", "初级(B)"))
        self.btn_adv.setText(_translate("Dialog", "高级(A)"))
        self.label_2.setText(_translate("Dialog", "注意，您稍后可以单击“游戏”菜单中“选项”来更改游戏难度级别。"))
        self.label.setText(_translate("Dialog", "您想从什么难度开始？"))
