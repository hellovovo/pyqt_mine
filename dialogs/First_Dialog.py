import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.gami_ui import Main_ui
from ui.simple_game import Ui_MainWindow
from ui.start_dialog import Ui_Dialog

simple = {'col':9,'row':9,'mine':10}
mid = {'col':15,'row':15,'mine':30}
adv = {'col':25,'row':25,'mine':99}

class FirstDialog(Ui_Dialog):
    def __init__(self,main_widget):
        self.main_widget = main_widget
        self.setupUi(main_widget)
        self.btn_simple.clicked.connect(self.simple_game)
        self.btn_mid.clicked.connect(self.mid_game)
        self.btn_adv.clicked.connect(self.adv_game)


    def simple_game(self):
        self.main_widget.close()
        self.main_window = QMainWindow()
        self.simple_game = Main_ui()
        self.simple_game.setupUi(self.main_window,simple)
        self.simple_game.init_connect()
        self.main_window.show()


    def mid_game(self):
        self.main_widget.close()
        self.main_window = QMainWindow()
        self.simple_game = Main_ui()
        self.simple_game.setupUi(self.main_window, mid)
        self.simple_game.init_connect()
        self.main_window.show()

    def adv_game(self):
        self.main_widget.close()
        self.main_window = QMainWindow()
        self.simple_game = Main_ui()
        self.simple_game.setupUi(self.main_window, adv)
        self.simple_game.init_connect()
        self.main_window.show()