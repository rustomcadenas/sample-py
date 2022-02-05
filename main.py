# import sys 
# from PyQt5.uic import loadUi
# from PyQt5.QtWidgets import QApplication

# from classes import LoginScreen
# from classes import WelcomeScreen 
 
# if __name__ == "__main__": 

#     def showLoginScreen():
#         login.show() 
#         # welcome.hide()

#     def showWelcomeScreen():
#         welcome.show()   
#         login.hide()

#     app = QApplication(sys.argv)

#     welcome = WelcomeScreen()
#     welcome.btn.clicked.connect(showLoginScreen)
#     welcome.show() 

#     login = LoginScreen() 
#     login.back.mousePressEvent = showWelcomeScreen

#     try:
#         sys.exit(app.exec())
#     except:
#         print("Program Terminated!")

import sys
from PyQt5.QtWidgets import QApplication

from classes import LoginScreen, WelcomeScreen, CreateAccountScreen

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

        # self.LoginScreen.btn_hideWidget.clicked.connect(self.hideWidget)
 
    # def hideWidget(self):
    #     if (self.LoginScreen.widget_login.isHidden()) == True :
    #         self.LoginScreen.widget_login.show()
    #     else:
    #         self.LoginScreen.widget_login.setVisible(False)


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
