import database
import time

class Shopping_List:
  def __init__(self,id):
    self.shopping = database.db.get(id)
  @staticmethod
  def new(user_id,ingredients):
    database.db.create({"user_id":user_id, "ingredients":ingredients, "date":time.time()})
  @staticmethod
  def all(user_id):
    ids = database.db.views.shopping_lists.all(key=user_id).ids()
    return [ Shopping_List(id) for id in ids ]
