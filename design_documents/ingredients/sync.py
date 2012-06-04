import couchquery
import os

db = couchquery.Database("http://hiclustescroblingletuall:csb5UthF3EFUXVH6xAChKTb0@hamiltop.cloudant.com/cs360")

db.sync_design_doc("ingredients", os.path.join(os.path.dirname(__file__), 'views'))
