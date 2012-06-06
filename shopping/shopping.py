from bottle import *
import time
from Shopping_List import Shopping_List
from users.users import require_login
from beaker.middleware import SessionMiddleware
import code

@route("/shopping/:id/delete", apply=require_login)
def shopping_delete(id): 
  session = request.environ["beaker.session"]
  shopping = Shopping_List(id)
  if shopping.shopping["user_id"] != session["user"]:
    if not "flash" in session:
      session["flash"] = {} 
    session["flash"]["error"]="You do not have permission to access that resource"
    redirect("/")
  else:
    if not "flash" in session:
      session["flash"] = {} 
    session["flash"]["success"]="Shopping List deleted successfully"
    shopping.delete()
    redirect("/shopping")

@route("/shopping/new", apply=require_login)
@view("shopping_form")
def new_shopping():
  return {}

@route("/shopping/:id/edit", apply=require_login)
@view("shopping_edit_form")
def shopping_edit(id):
  session = request.environ["beaker.session"]
  shopping = Shopping_List(id)
  if shopping.shopping["user_id"] != session["user"]:
    if not "flash" in session:
      session["flash"] = {} 
    session["flash"]["error"]="You do not have permission to access that resource"
    redirect("/")
  else:
    return shopping.shopping 

@post("/shopping/:id/update")
def update_shopping(id):
  session = request.environ["beaker.session"]
  shopping = Shopping_List(id)
  if shopping.shopping["user_id"] != session["user"]:
    if not "flash" in session:
      session["flash"] = {} 
    session["flash"]["error"]="You do not have permission to access that resource"
    redirect("/")
  else:
    ingredients = []
    for i in range(10):
      name = request.forms.get("ingredient[%d][name]" % i)
      unit = request.forms.get("ingredient[%d][unit]" % i)
      quantity = request.forms.get("ingredient[%d][quantity]" % i)
      price = request.forms.get("ingredient[%d][price]" % i)
      if name != "" and quantity != "" and int(quantity) > 0:
        ingredients.append({"name":name,"unit":unit,"quantity":quantity,"price":price})
    shopping.shopping["ingredients"] = ingredients
    shopping.save()
    if not "flash" in session:
      session["flash"] = {} 
    session["flash"]["success"]="Shopping List updated successfully"
    redirect("/shopping/"+id) 

@post("/shopping", apply=require_login)
def create_shopping():
  session = request.environ["beaker.session"]
  ingredients = []
  for i in range(10):
    name = request.forms.get("ingredient[%d][name]" % i)
    unit = request.forms.get("ingredient[%d][unit]" % i)
    quantity = request.forms.get("ingredient[%d][quantity]" % i)
    price = request.forms.get("ingredient[%d][price]" % i)
    if name != "" and quantity != "" and int(quantity) > 0:
      ingredients.append({"name":name,"unit":unit,"quantity":quantity,"price":price})
  Shopping_List.new(session["user"],ingredients)
  if not "flash" in session:
    session["flash"] = {} 
  session["flash"]["success"]="Shopping List saved successfully"
  redirect("/") 

@route("/shopping/:id", apply=require_login)
@view("show_shopping")
def show_shopping(id):
  session = request.environ["beaker.session"]
  shopping = Shopping_List(id)
  if shopping.shopping["user_id"] != session["user"]:
    if not "flash" in session:
      session["flash"] = {} 
    session["flash"]["error"]="You do not have permission to access that resource"
    redirect("/")
  else:
    shopping.shopping["cost"] = shopping.cost
    return shopping.shopping 

@get("/shopping", apply=require_login)
@view("shopping_index.tpl")
def shopping_index():
  session = request.environ["beaker.session"]
  lists = Shopping_List.all(session["user"])
  return {"lists":lists}
