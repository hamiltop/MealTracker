from bottle import *
from Shopping_List import Shopping_List
from users.users import require_login
from beaker.middleware import SessionMiddleware

@route("/shopping/new")
@view("shopping_form")
def new_shopping():
  require_login()
  return {}

@post("/shopping")
def create_shopping():
  ingredients = []
  for i in range(10):
    name = request.forms.get("ingredient[%d][name]" % i)
    unit = request.forms.get("ingredient[%d][unit]" % i)
    quantity = request.forms.get("ingredient[%d][quantity]" % i)
    price = request.forms.get("ingredient[%d][price]" % i)
    if name != "":
      ingredients.append({"name":name,"unit":unit,"quantity":quantity,"price":price})
  Shopping_List.new(request.environ["beaker.session"]["user"],ingredients)
  redirect("/") 

