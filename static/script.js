function mode() {
    const km = parseFloat(document.getElementById('travel').value);
    const fuel = parseFloat(document.getElementById('fuel').value);
    const price = parseFloat(document.getElementById('price').value);
    const passengers = parseFloat(document.getElementById('passengers').value) || 1;
    const allprice = (km / 100) * fuel * price;
    const persons = allprice / passengers;
    document.getElementById('total').innerText = "Total: " + allprice.toFixed(2) + "€ | Per person: " + persons.toFixed(2) + "€";
}
