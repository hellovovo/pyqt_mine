from PyQt5.QtCore import QPoint

from ui.simple_game import Ui_MainWindow


class Main_ui(Ui_MainWindow):
    def __init__(self):

        pass

    def init_connect(self):
        self.actionnew_game.triggered.connect(self.widget.init_data)