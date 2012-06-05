import database
from users.users import *

class Ingredient:
  def __init__(self, name, unit):
    user_id = current_user_id()
    print name, unit
    ingredient = database.db.views.ingredients.ingredient_average(
      startkey=[user_id, name, unit],
      endkey=[user_id, name, unit, {}],
      group=True
    ).values()[0]
    self.price = float(ingredient[0])/ingredient[1]
  @staticmethod
  def averages(user_id):
    return database.db.views.ingredients.ingredient_average(
      startkey=[user_id],
      endkey=[user_id,{}],
      group_level=3
    ).items()
  @staticmethod
  def all(user_id):
    ingredients =  database.db.views.ingredients.ingredient_average(
      startkey=[user_id],
      endkey=[user_id,{}],
      reduce=False
    )
    ids = ingredients.ids()
    items = ingredients.items()
    array = []
    for x in xrange(len(items)):
      array.append({
        "id":ids[x],
        "name":items[x][0][1], 
        "unit":items[x][0][2],
        "date":time.asctime(time.localtime(items[x][0][3])),
        "quantity":items[x][1][1],
        "price":items[x][1][0] })
    return array
