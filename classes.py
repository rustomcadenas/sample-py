from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QCursor
 
 
class WelcomeScreen(QDialog):
    def __init__(self): 
        super(WelcomeScreen, self).__init__()
        loadUi("ui/welcome.ui", self)
        
        self.btn_login.setCursor(QCursor(QtCore.Qt.PointingHandCursor))  
        self.btn_create_account.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
  
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("ui/login.ui", self)

        self.btn_back.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_loggingin.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

class CreateAccountScreen(QDialog):
    def __init__(self):
        super(CreateAccountScreen, self).__init__()
        loadUi("ui/create_account.ui", self)

        self.nput_fullname.setPlaceholderText("Juan Dela Cruz")
        self.btn_create_account.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setCursor(QCursor(QtCore.Qt.PointingHandCursor))