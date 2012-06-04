function(keys,values,rereduce){
  prices = 0;
  count = 0;
  for(i in values){
    prices += values[i][0]
    count +=  values[i][1]
  }
  return [prices, count] 
}
