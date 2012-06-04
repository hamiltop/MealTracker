from bottle import *
import database
import code
from User import User

@get("/users/new")
@view("new_user_form")
def new_user():
  return {}

@post("/users")
def create_user():
  name = request.forms.get('username')
  password = request.forms.get('password')
  user = User.new(name,password)
  login_helper(user)
  redirect("/")

@get("/users/login")
@view("login_form_full") 
def get_login_form():
  username = request.forms.get('username')
  if username == None:
    username = ""
  return {"username":username}  

@post("/users/session")
def create_session():
  name = request.forms.get('username')
  password = request.forms.get('password')
  user = User.login(name,password)
  login_helper(user)
  redirect("/")

@get("/users/logout", name="logout")
def destroy_session():
  login_helper(sign_out=True)
  redirect("/")
   
def login_helper(user=None, sign_out=False):
  session=request.environ["beaker.session"]
  if not "flash" in session:
    session["flash"] = {}
  if user != None:
    session["user"] = user.user._id
    session["flash"]["success"] = "Login Successful"
    return True
  else:
    if "user" in session:
      del session["user"]
    if not "flash" in session:
      session["flash"] = {}
    if not sign_out:
      session["flash"]["error"] = "Unsuccessful Login"
    else:
      session["flash"]["success"] = "Successfully logged out"
    return False

def current_user():
  session=request.environ["beaker.session"]
  if "user" in session:
    user_id = session["user"]
    return User(user_id)
  else:
    return None

def current_user_id():
  session=request.environ["beaker.session"]
  if "user" in session:
    return session["user"]
  else:
    return None

def logged_in():
  return current_user() != None    

def require_login(target):
  def _require_login():
    session=request.environ["beaker.session"]
    if not logged_in():
      if not "flash" in session:
        session["flash"] = {}
      session["flash"]["error"] = "You must be logged in to get to that page"
      redirect("/")
      return None
    else:
      return target()
  return _require_login
