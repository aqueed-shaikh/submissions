var i = 0;
var elt = document.getElementsByTagName('li');
var next = function(e){
    elt[i % elt.length].classList.toggle('green');
    i++;
    elt[i % elt.length].classList.toggle('green');
}

    var button = document.getElementById('press');
button.addEventListener('click',next);

