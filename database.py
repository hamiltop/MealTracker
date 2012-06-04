import couchquery

print "Getting DB object"
db = couchquery.Database("http://hiclustescroblingletuall:csb5UthF3EFUXVH6xAChKTb0@hamiltop.cloudant.com/cs360")
try:
  db.views.shopping_lists
except AttributeError:
  pass
try:
  db.views.ingredients
except AttributeError:
  pass
try:
  db.views.users
except AttributeError:
  pass
