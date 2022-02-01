 
import sys 
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget
from PyQt5.QtGui import QCursor

class WelcomeScreen(QDialog):
    def __init__(self): 
        super(WelcomeScreen, self).__init__()
        loadUi("sample.ui", self)
        self.btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
 
        self.buttonCreateAcc.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome = WelcomeScreen()
    widget = QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(541)
    widget.setFixedWidth(731)
    widget.show()
    try:
        sys.exit(app.exec())
    except:
        print("Program Terminated!")

