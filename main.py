from PyQt5 import QtWidgets
from src.application.case import MyApplication
import sys


app = QtWidgets.QApplication([])
application = MyApplication()
application.show()

sys.exit(app.exec())