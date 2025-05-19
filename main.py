from PyQt5 import QtWidgets
from src.application.case import MainWindow
import sys


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())