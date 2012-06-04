from bottle import *
import database
import code
from ingredients.Ingredient import *

@get("/meals/new")
@view("new_meal_form")
def new_meal():
  return {}

@post("/meals/cost")
def meal_cost():
  ingredients = []
  cost = 0
  for i in range(10):
    name = request.forms.get("ingredient[%d][name]" % i)
    unit = request.forms.get("ingredient[%d][unit]" % i)
    quantity = request.forms.get("ingredient[%d][quantity]" % i)
    if name != "":
      ingredient = Ingredient(name,unit)
      cost += ingredient.price * float(quantity)
  return str(cost)
