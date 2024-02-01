from database.database import db_connection
from .entities.user_entitie import User

class UserModel:

    @classmethod
    def getUsers(self):
        try:
            connection = db_connection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM USERS ORDER BY username ASC")
                result = cursor.fetchall()

                for row in result:
                    user = User(row[0], row[1], row[2], row[3])
                    users.append(user.convertJSON())

            connection.close()
            return users

        except Exception as error:
            raise Exception(error)
    
    @classmethod
    def addUser(self, user):
        try:
            connection = db_connection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO USERS (id, username, email, login_date) VALUES (%s, %s, %s, CURRENT_DATE())", (user.id, user.username, user.email))
                result = cursor.rowcount
                connection.commit()

            connection.close()
            return result
        except Exception as error:
            raise Exception(error)
    
    @classmethod
    def deleteUser(self, id):
        try:
            connection = db_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM USERS WHERE id=%s", (id))
                result = cursor.rowcount
                connection.commit()

            connection.close()
            return result  
        except Exception as error:
            return Exception(error)
        
    @classmethod
    def updateUser(self, user):
        try:
            connect = db_connection()

            with connect.cursor() as cursor:
                cursor.execute("UPDATE USERS SET username=%s, email=%s WHERE id=%s", (user.username, user.email, user.id))
                result = cursor.rowcount
                connect.commit()

            connect.close()
            return result
        except Exception as error:
            return Exception(error)
    
    @classmethod
    def getUserDate(self, id):
        try:
            connect = db_connection()

            with connect.cursor() as cursor:
                cursor.execute("SELECT login_date FROM USERS WHERE id=%s", (id))
                user_date = cursor.fetchone()
            
            connect.close()
            return user_date[0]
        except Exception as error:
            return Exception(error)