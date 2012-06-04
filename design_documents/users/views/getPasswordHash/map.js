function(doc) {
  if(doc.username && doc.password){
    emit(doc.username, doc.password);
  }
}
