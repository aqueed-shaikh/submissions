var item = 0;
var pokemon = document.querySelectorAll('li');
var button = document.getElementById('b1');

var grass = function(e) {
	this.classList.toggle('green');
}
var fire = function(e) {
	this.classList.toggle('red');
}
var water = function(e) {
	this.classList.toggle('blue');
}

var next = function(e) {
	console.log(e);
	if (item%3 == 0)
		pokemon[item%pokemon.length].classList.toggle('green');
	else if (item%3 == 1)
		pokemon[item%pokemon.length].classList.toggle('red');
	else
		pokemon[item%pokemon.length].classList.toggle('blue');
	item++;
}

for (var i = 0; i < pokemon.length; i++) {
	if (i%3 == 0)
		pokemon[i].addEventListener('click', grass);
	else if (i%3 == 1)
		pokemon[i].addEventListener('click', fire);
	else
		pokemon[i].addEventListener('click', water);
}
button.addEventListener('click',next);