from bottle import *
import database
import code
from ingredients.Ingredient import *
from users.users import *
import time
from Meal import Meal

@get("/meals/new", apply=require_login)
@view("new_meal_form")
def new_meal():
  ingredients = Ingredient.averages(current_user_id())
  names = [ x[0][1] for x in ingredients ]
  units = list(set([ x[0][2] for x in ingredients ]))
  return {"names":names, "units":units}

@post("/meals", apply=require_login)
def create_meal():
  session = request.environ["beaker.session"]
  ingredients = []
  cost = 0
  name = request.forms.get("name")
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
  if not "flash" in session:
    session["flash"] = {} 
  session["flash"]["success"]="Meal created successfully"
  meal = Meal.new(session["user"],ingredients,name)
  redirect("/meals/"+meal.meal["_id"])

@route("/meals/:id")
@view("meal_cost")
def meal_cost(id):
  session = request.environ["beaker.session"]
  meal = Meal(id)
  if meal.meal["user_id"] != session["user"]:
    if not "flash" in session:
      session["flash"] = {} 
    session["flash"]["error"]="You do not have permission to access that resource"
    redirect("/")
  else:
    return {"ingredients":meal.meal.meal, "cost":meal.cost, "id":meal.meal._id}

@get("/meals")
@view("meal_index")
def meal_index():
  session = request.environ["beaker.session"]
  meals = Meal.all(session["user"])
  return {"meals":meals}

@route("/meals/:id/delete", apply=require_login)
def meals_delete(id):
  session = request.environ["beaker.session"]
  meal = Meal(id)
  if meal.meal["user_id"] != session["user"]:
    if not "flash" in session:
      session["flash"] = {} 
    session["flash"]["error"]="You do not have permission to access that resource"
    redirect("/")
  else:
    if not "flash" in session:
      session["flash"] = {} 
    session["flash"]["success"]="Meal deleted successfully"
    meal.delete()
    redirect("/meals")
  
