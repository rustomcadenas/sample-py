import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

from classes import LoginScreen, WelcomeScreen, CreateAccountScreen, MainScreen
from db import DB

class Main():
    def __init__(self):
        super(Main, self).__init__() 


        self.WelcomeScreen = WelcomeScreen()    #Welcome Screen
        self.WelcomeScreen.show()
        self.WelcomeScreen.btn_login.clicked.connect(self.openLoginScreen)
        self.WelcomeScreen.btn_create_account.clicked.connect(self.openCreateAccountScreen)

        self.LoginScreen = LoginScreen()    #Login Screen         
        self.LoginScreen.btn_loggingin.clicked.connect(self.loggedIn)
        self.LoginScreen.btn_back.clicked.connect(self.openWelcomeScreen)
        self.LoginScreen.txt_password.returnPressed.connect(self.loggedIn)

        self.CreateAccountScreen = CreateAccountScreen()    #Create Account Screen
        self.CreateAccountScreen.btn_back.clicked.connect(self.openWelcomeScreen)
        self.CreateAccountScreen.btn_create_account.clicked.connect(self.createAccount)

        self.MainScreen = MainScreen()  #Main Screen
        # self.MainScreen.setVisible(True)
        self.MainScreen.btn_sample.clicked.connect(self.displayMessage)
        
    def displayMessage(self): 
        msg = QMessageBox()
        msg.setText("This is a message box")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec()

    def createAccount(self):
        fname = self.CreateAccountScreen.nput_fullname.text()
        course = self.CreateAccountScreen.nput_course.currentText()
        bday = self.CreateAccountScreen.nput_bday.date().toPyDate()
        username = self.CreateAccountScreen.nput_username.text()
        password = self.CreateAccountScreen.nput_password.text()
        data = fname, course, bday, username, password
        db = DB()
        db.query("INSERT INTO tbl_users(fullname, course, bday, username, password) VALUES (%s, %s, %s, %s, %s)", data)
        # print("{} | {}, {} | {} | {}".format(fname, course, bday, username, password)) 
        self.clearCreateAccountFields()


    def clearCreateAccountFields(self):
        self.CreateAccountScreen.nput_fullname.setText("")

    def loggedIn(self):    
        name = self.LoginScreen.txt_username.text()
        password = self.LoginScreen.txt_password.text()
        

        if name == "tomas" and password == "gwapo":
            self.LoginScreen.lbl_error.setText("Ttomas gwapo")
        elif name == "" and password == "":
            self.LoginScreen.lbl_error.setText("Username or password is empty.")
        else :
            self.LoginScreen.lbl_error.setText("Invalid username or password.")

    def openWelcomeScreen(self):
        self.WelcomeScreen.show()
        self.LoginScreen.hide()
        self.CreateAccountScreen.hide()

    def openLoginScreen(self):        
        self.LoginScreen.show()
        self.WelcomeScreen.hide() 

    def openCreateAccountScreen(self):
        self.CreateAccountScreen.show()
        self.WelcomeScreen.hide()
 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    try:
        sys.exit(app.exec())
    except:
        print("Program Terminated!")
