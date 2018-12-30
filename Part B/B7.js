document.getElementById("car1").addEventListener("mouseover", myFunction2);
document.getElementById("car2").addEventListener("mouseover", myFunction3);

function myFunction2() {
    var myObj, i, x = " ", y=" ";
    document.getElementById("MenuTable").removeAttribute('hidden');
    myObj = {
        "name":"FERRARI SERIES",
       
       
        "ingredients":[ "NAME=ferrari", "MODEL=a", "PRICE=2.5cr", "YEAR=2015"]
    };
y = myObj.name;
  for (i in myObj.ingredients) {
      x += myObj.ingredients[i] + "&nbsp";
  }

      z = myObj.image_name;
  document.getElementById("item1").innerHTML = y;
  document.getElementById("item2").innerHTML = x;
  document.getElementById("item3").innerHTML = '<img src="brownie.jpeg"/>';
}

function myFunction3() {
    document.getElementById("MenuTable").removeAttribute('hidden');
    var myObj, i, x = " ", y=" ";
    myObj = {
        "name":"BMW SERIES",
       // "image_name": "brownie
        "ingredients":[ "NAME=BMW", "NAME=B", "PRICE=2 CR", "YEAR=2016"]
    };
y = myObj.name;
  for (i in myObj.ingredients) {
      x += myObj.ingredients[i] + "&nbsp";
  }

      z = myObj.image_name;
      document.getElementById("item1").innerHTML = y;
      document.getElementById("item2").innerHTML = x;
      document.getElementById("item3").innerHTML = '<img src="strawberry.jpeg"/>';
}
