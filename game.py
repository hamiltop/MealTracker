from bottle import *
import database
from player import Player
import code
from users import users
from beaker.middleware import SessionMiddleware
from shopping import shopping
from ingredients.Ingredient import *
from ingredients import ingredients
from meals import meals

@route("/static/:path#.+#", name='static')
def static(path):
  return static_file(path, root='static')

@route("/bootstrap/:path#.+#", name='bootstrap')
def bootstrap(path):
  return static_file(path, root='bootstrap')

@route("/")
@view("index")
def index():
  user = users.current_user()
  return {"title":"Meal Tracker"}

@route("/test")
@require_login
def test():
  i = Ingredient("Apples","item")
  print i.price
  return str(i.price)


session_opts = {
    "session.type": "file",
    'session.cookie_expires': True,
    'session.auto': True,
    'session.data_dir': "cache",
}

  

debug()
app = default_app()
def bottle_flash():
  import bottle
  session=bottle.request.environ["beaker.session"]
  if "flash" in session:
    f = session["flash"].copy()
    session["flash"].clear()
    return f
  else:
    return {}

SimpleTemplate.defaults["get_url"] = app.get_url
SimpleTemplate.defaults["current_user"] = users.current_user
SimpleTemplate.defaults["interact"] = code.interact
SimpleTemplate.defaults["flash"] = bottle_flash

app = SessionMiddleware(app, session_opts)
run(app=app,reloader=True)