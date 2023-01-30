from ... import adminDB
from enum import Enum

class User(adminDB.Model):
     __tablename__ = 'users'
     id = adminDB.Column(adminDB.Integer, primary_key = True)
     username = adminDB.Column(adminDB.String(45), unique = True, nullable = False)
     email = adminDB.Column(adminDB.String(50), unique = True, nullable = False)
     password_hash = adminDB.Column(adminDB.Text(), nullable = False)
     is_admin = adminDB.Column(adminDB.Boolean(), default = False)
     is_active = adminDB.Column(adminDB.Boolean(), default = True)
     
     def __repr__(self):
          return f"User : {self.username}"    
