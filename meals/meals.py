from bottle import *
import database
import code
from ingredients.Ingredient import *
from users.users import *

@get("/meals/new")
@view("new_meal_form")
def new_meal():
  ingredients = Ingredient.averages(current_user_id())
  names = [ x[0][1] for x in ingredients ]
  units = list(set([ x[0][2] for x in ingredients ]))
  return {"names":names, "units":units}

@post("/meals/cost")
@view("meal_cost")
def meal_cost():
  ingredients = []
  cost = 0
  for i in range(10):
    name = request.forms.get("ingredient[%d][name]" % i)
    unit = request.forms.get("ingredient[%d][unit]" % i)
    quantity = request.forms.get("ingredient[%d][quantity]" % i)
    if quantity != "":
      ingredient = Ingredient(name,unit)
      cost += ingredient.price * float(quantity)
      ingredients.append({
        "name":name,
        "unit":unit,
        "quantity":quantity,
        "price":ingredient.price,
        "cost":ingredient.price * float(quantity)
      })
  return {"ingredients":ingredients, "cost":cost}
