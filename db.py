import mysql.connector 

class DB:
    def __init__(self):
        self.db_host = 'localhost'
        self.db_name = 'py_crud'
        self.db_user = 'root'
        self.db_password = '' 
 
    def query(self, query, params):
        self.connection = mysql.connector.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_password)

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


 