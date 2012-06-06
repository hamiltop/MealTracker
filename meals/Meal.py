import database 
import time
import code

class Meal:
  def __init__(self, id):
    self.meal = database.db.get(id)
    self.cost = sum([ float(x["cost"]) for x in self.meal["meal"] ])
  @staticmethod
  def new(user_id,ingredients,name):
    meal = database.db.create({"user_id":user_id, "meal":ingredients, "date":time.time(), "name":name})
    return Meal(meal["id"]) 
  @staticmethod
  def all(user_id):
    ids = database.db.views.meals.all(key=user_id).ids()
    return [ Meal(id) for id in ids ]
  def delete(self):
    database.db.delete(self.meal)
