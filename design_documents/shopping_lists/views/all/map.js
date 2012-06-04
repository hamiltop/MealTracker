function(doc){
  if(doc.user_id && doc.ingredients){
    emit(doc.user_id,doc._id)
  }
}
