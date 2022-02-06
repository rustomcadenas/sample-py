import mysql.connector 

class DB:
    def __init__(self):
        db_host = 'localhost'
        db_name = 'py_crud'
        db_user = 'root'
        db_password = ''
        self.connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)


        if self.connection.is_connected():
            print("Connection is successful")
        else:
            print("Connection Failed")


    def query(self, query, params):
        splitted_query = query.split()[0]

        try: 
            cursor = self.connection.cursor(prepared=True)
            cursor.execute(query, params)
            
            if splitted_query == "select":
                records = cursor.fetchall()
                return records 
            else:
                self.connection.commit()  

        except mysql.connector.Error as error:
            print ("Parameterize query failed: {}". format(error))
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                print("Mysql Connection is close")

db = DB()
data = 'Joharah Gwapa', 'ABCD', '1997/1/1', 'username', 'password'
db.query("INSERT INTO tbl_users(fullname, course, bday, username, password) VALUES (%s, %s, %s, %s, %s)", data)

# data = 'Tom Gwapo', 'BS INFO TECH', 1
# db.query("UPDATE tbl_users set fullname=%s, course=%s where user_id=%s", data)

# print(db.query("select * from tbl_users", ""))