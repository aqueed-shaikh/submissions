var i = 0;
var highlight = function(e){
    var elements = document.querySelectorAll('li');
    if (i!=0)
	elements[(i-1)%10].classList.toggle('highlight');
    elements[i%10].classList.toggle('highlight');
    i++;
}

var b = document.getElementById('btn');
b.addEventListener('click',highlight);