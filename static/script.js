document.getElementById('mode').addEventListener'click', function()){
  const km= parseFloat(document.getElementById('travel').value);
  const fuel = parseFloat(document.getElementById('fuel').value);
  const price=parseFloat(document.getElementById('price').value);
  const passengers=parseFloat(document.getElementById('passengers').value);
  const allprice=(km / 100) * fuel * price;
  const persons= allprice / passengers ;
  document.getElementById('total').innerText="total" + allprice.toFixed(2) + "€\n";
  "oneperson" + persons.toFixed(2) +"€";
});