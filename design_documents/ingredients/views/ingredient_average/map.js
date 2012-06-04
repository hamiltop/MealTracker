function(doc) {
  if(doc.ingredients){
    for(i in doc.ingredients){
      var ingredient = doc.ingredients[i];
      if(ingredient.quantity && ingredient.unit && ingredient.name && ingredient.price){
        emit([doc.user_id, ingredient.name, ingredient.unit ], [parseFloat(ingredient.price), parseFloat(ingredient.quantity)]);
      }
    }
  }
}
