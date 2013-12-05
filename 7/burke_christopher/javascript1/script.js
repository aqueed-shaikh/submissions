var counter = 0;
var listitems = document.querySelectorAll('li');

var activate = function(e) {
    listitems[counter % listitems.length].classList.toggle('large');
    listitems[counter % listitems.length].classList.toggle('center');
    listitems[counter % listitems.length].classList.toggle('red');
    counter++;
    listitems[counter % listitems.length].classList.toggle('large');
    listitems[counter % listitems.length].classList.toggle('center');
    listitems[counter % listitems.length].classList.toggle('red');
}

var button = document.querySelectorAll('input');

button[0].addEventListener('click',activate);


listitems[0].classList.toggle('large');
listitems[0].classList.toggle('center');
listitems[0].classList.toggle('red');
