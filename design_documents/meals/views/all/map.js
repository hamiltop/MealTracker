function(doc){
  if(doc.meal && doc.user_id){
    emit(doc.user_id,doc)
  } 
}
