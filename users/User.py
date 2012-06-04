import database
import code
import bcrypt
 
class User:
  def __init__(self, id):
    self.user = database.db.get(id)
  @staticmethod
  def login(username, password):
    user = database.db.views.users.getPasswordHash(key=username)
    if len(user) == 1 and bcrypt.hashpw(password, user[0]) == user[0]:
      return User(user.ids()[0])
    else:
      return None

  @staticmethod
  def new(username, password):
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    user = database.db.create({"_id":username,"username":username,"password":password})
    return User(user["id"])
       
    
