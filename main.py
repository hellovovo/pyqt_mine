from PyQt5.QtWidgets import QApplication, QWidget, QDialog
import sys

from dialogs.First_Dialog import FirstDialog
from ui.start_dialog import Ui_Dialog

if __name__=='__main__':
    app = QApplication(sys.argv)
    # main_window = QWidget()
    widget = QWidget()
    # widget = QDialog()
    dialog = FirstDialog(widget)
    widget.show()
    sys.exit(app.exec_())
