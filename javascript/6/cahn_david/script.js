window.onload=starter ();

function starter () {
    var list =  document.querySelectorAll('li');
    list[0].classList.add ('red');
    currentColor = 0;
}

var colorNextElement = function() {
    var list =  document.querySelectorAll('li');
    if (currentColor === list.length - 1) {
	list [currentColor].classList.remove ('red')
	return starter ();
}
    list [currentColor].classList.remove ('red')
    currentColor = currentColor + 1;
    list [currentColor].classList.add ('red');
}

var colorPreviousElement = function() {
    var list =  document.querySelectorAll('li');
    var len = list.length;
    if (currentColor === 0) {
	list [currentColor].classList.remove ('red');
	currentColor = 5;
	list [currentColor].classList.add ('red');
	return;
}
    list [currentColor].classList.remove ('red')
    currentColor = currentColor - 1;
    list [currentColor].classList.add ('red');
}

document.getElementById("button1").addEventListener("click",colorNextElement);
document.getElementById("button2").addEventListener("click",colorPreviousElement);

