function (doc){
  if(doc.order){
    emit([doc.username,doc.timestamp], doc.price)
  }
}
