import database
from users.users import *

class Ingredient:
  def __init__(self, name, unit):
    user_id = current_user_id()
    ingredient = database.db.views.ingredients.ingredient_average(
      key=[user_id, name, unit],
      group=True
    ).values()[0]
    self.price = float(ingredient[0])/ingredient[1]
  @staticmethod
  def averages(user_id):
    return database.db.views.ingredients.ingredient_average(
      startkey=[user_id],
      endkey=[user_id,{}],
      group=True
    ).items()
  @staticmethod
  def all(user_id):
    ingredients =  database.db.views.ingredients.ingredient_average(
      startkey=[user_id],
      endkey=[user_id,{}],
      reduce=False
    ).items()
    return [ {
      "name":i[0][1], 
      "unit":i[0][2],
      "quantity":i[1][1],
      "price":i[1][0] } for i in ingredients ]
