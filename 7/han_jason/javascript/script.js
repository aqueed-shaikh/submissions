var blue = function(e) {
    console.log(e);
    elts[i].classList.toggle('blue');
    i++;
    if (i >= elts.length) i = 0;
    elts[i].classList.toggle('blue');
}

var elts = document.querySelectorAll('li');
elts[0].classList.toggle('blue');
var i = 0;
var button = document.getElementById('b1');
button.addEventListener('click', blue);
