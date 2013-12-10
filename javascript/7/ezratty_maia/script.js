var green=function(e) {
    console.log(e);
    this.classList.toggle('green');
}

var i = 0;
var cycle = function(e) {
    console.log(e);
    var items = document.querySelectorAll('li');
    items[i%items.length].classList.toggle('green');
    items[(i+1)%items.length].classList.toggle('green');
    i++;
}

var items = document.querySelectorAll('li');
items[0].classList.add('green');
var button = document.getElementById('b1');
button.addEventListener('click',cycle);