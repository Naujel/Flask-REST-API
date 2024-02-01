from datetime import datetime

class User:
    def __init__(self, id, username=None, email=None, date=None):
        self.id = id
        self.username = username
        self.email = email
        self.date = date
    
    def convertJSON(self):
        return {
            'id':self.id,
            'username':self.username,
            'email':self.email,
            'date':datetime.strftime(self.date, "%d-%m-%y")
        }