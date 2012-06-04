from bottle import *
import database
import code
from Ingredient import Ingredient
from users.users import *

@route("/ingredients", apply=require_login)
@view("ingredients_list")
def ingredient_summary():
  i = Ingredient.averages(current_user_id())
  a = Ingredient.all(current_user_id())
  print i
  print a
  return {"averages":i, "all":a} 
