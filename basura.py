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



# ========================
# db = DB()
# data = 'Joharah Gwapa', 'ABCD', '1997/1/1', 'username', 'password'
# db.query("INSERT INTO tbl_users(fullname, course, bday, username, password) VALUES (%s, %s, %s, %s, %s)", data)

# # data = 'Tom Gwapo', 'BS INFO TECH', 1
# # db.query("UPDATE tbl_users set fullname=%s, course=%s where user_id=%s", data)

# print(db.query("select * from tbl_users", ""))