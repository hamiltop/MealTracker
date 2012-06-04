import database

class Shopping_List:
  @staticmethod
  def new(user_id,ingredients):
    database.db.create({"user_id":user_id, "ingredients":ingredients})
