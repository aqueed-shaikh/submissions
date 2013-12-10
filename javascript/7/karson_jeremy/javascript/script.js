var i = 0;
var items = document.querySelectorAll('li');
items[i].classList.toggle('blue');

var inc = function(e){
    console.log(e);
    items[i].classList.toggle('blue');
    if (i < items.length - 1)
	i++;
    else
	i = 0;
    items[i].classList.toggle('blue');
}

var dec = function(e){
    console.log(e);
    items[i].classList.toggle('blue');
    if (i > 0)
	i--;
    else
	i = items.length - 1;
    items[i].classList.toggle('blue');
}

var fwd = document.getElementById('b1');
fwd.addEventListener('click', inc);
var bckwd = document.getElementById('b2');
bckwd.addEventListener('click', dec);
