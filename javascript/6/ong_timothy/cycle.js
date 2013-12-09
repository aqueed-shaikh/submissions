var count = 0;

var cycle = function(e){
    elts[(count%6)].classList.toggle('green');
    elts[((count+1)%6)].classList.toggle('green');
    count++;
}

var elts = document.querySelectorAll('li');
var button = document.getElementById('cycle');
button.addEventListener('click',cycle);

