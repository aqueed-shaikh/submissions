var g = 0;
var b = 1;
var r = 2;
var change = function(e){
    console.log(e);
    var li = document.querySelectorAll('li');
    li[g++].classList.toggle('green');
    li[b++].classList.toggle('blue');
    li[r++].classList.toggle('red'); 
    if (g === li.length)
	g = 0;
    if (b === li.length)
	b = 0;
    if (r === li.length)
	r = 0;
    li[g].classList.toggle('green');
    li[b].classList.toggle('blue');
    li[r].classList.toggle('red');
}
    

var button = document.getElementById('changer');
button.addEventListener('click', change);