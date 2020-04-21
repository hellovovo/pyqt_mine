# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_game.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from widgets.Simple_gaem_Widget import SimpleWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(237, 292)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = SimpleWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.widget.setStyleSheet("QWidget{\n"
"    background-color:#ccc\n"
"}")
        self.widget.setObjectName("widget")
        self.label_timer = QtWidgets.QLabel(self.centralwidget)
        self.label_timer.setGeometry(QtCore.QRect(34, 229, 30, 30))
        self.label_timer.setText("")
        self.label_timer.setPixmap(QtGui.QPixmap("../imgs/timer.png"))
        self.label_timer.setScaledContents(True)
        self.label_timer.setObjectName("label_timer")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(78, 236, 18, 20))
        self.label_time.setObjectName("label_time")
        self.label_cnt = QtWidgets.QLabel(self.centralwidget)
        self.label_cnt.setGeometry(QtCore.QRect(170, 236, 16, 16))
        self.label_cnt.setObjectName("label_cnt")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(190, 231, 25, 25))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../imgs/lei.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 237, 23))
        self.menubar.setObjectName("menubar")
        self.menu_game = QtWidgets.QMenu(self.menubar)
        self.menu_game.setObjectName("menu_game")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.actionnew_game = QtWidgets.QAction(MainWindow)
        self.actionnew_game.setObjectName("actionnew_game")
        self.actioncount = QtWidgets.QAction(MainWindow)
        self.actioncount.setObjectName("actioncount")
        self.actionoptions = QtWidgets.QAction(MainWindow)
        self.actionoptions.setObjectName("actionoptions")
        self.actionlook = QtWidgets.QAction(MainWindow)
        self.actionlook.setObjectName("actionlook")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionshow_help = QtWidgets.QAction(MainWindow)
        self.actionshow_help.setObjectName("actionshow_help")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionabout_2 = QtWidgets.QAction(MainWindow)
        self.actionabout_2.setObjectName("actionabout_2")
        self.actionmore_game = QtWidgets.QAction(MainWindow)
        self.actionmore_game.setObjectName("actionmore_game")
        self.menu_game.addAction(self.actionnew_game)
        self.menu_game.addSeparator()
        self.menu_game.addAction(self.actioncount)
        self.menu_game.addAction(self.actionoptions)
        self.menu_game.addAction(self.actionlook)
        self.menu_game.addSeparator()
        self.menu_game.addAction(self.actionexit)
        self.menu_help.addAction(self.actionshow_help)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.actionabout_2)
        self.menu_help.addAction(self.actionmore_game)
        self.menubar.addAction(self.menu_game.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "扫雷"))
        self.label_time.setText(_translate("MainWindow", "240"))
        self.label_cnt.setText(_translate("MainWindow", "10"))
        self.menu_game.setTitle(_translate("MainWindow", "游戏(G)"))
        self.menu_help.setTitle(_translate("MainWindow", "帮助(H)"))
        self.actionnew_game.setText(_translate("MainWindow", "新游戏(N)    F2"))
        self.actioncount.setText(_translate("MainWindow", "统计信息(S)  F4"))
        self.actionoptions.setText(_translate("MainWindow", "选项(O)  F5"))
        self.actionlook.setText(_translate("MainWindow", "更改外观(A)  F7"))
        self.actionexit.setText(_translate("MainWindow", "退出(X)"))
        self.actionshow_help.setText(_translate("MainWindow", "查看帮助(V)  F1"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actionabout_2.setText(_translate("MainWindow", "关于扫雷(A)"))
        self.actionmore_game.setText(_translate("MainWindow", "联机获得更多游戏(M)"))


