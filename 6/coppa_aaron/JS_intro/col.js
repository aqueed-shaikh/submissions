i=0
lastI=0
items = document.querySelectorAll("li");

for(var j = 0; j < items.length; j++) {
//      items[j].style.size = 100;
}
var colorize = function() {
  console.log("I: " + i)
  items[lastI].style.color = "";
  items[i].style.color = 'red'; //('red');
  lastI = i;
  i = (i + 1) % items.length;
}

document.querySelectorAll("h1")[0].addEventListener('click', colorize);

