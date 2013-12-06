var i = 0;
var items = document.getElementsByTagName('li');
var alternater = function(e){    
    items[i % items.length].classList.toggle('blue');
    i++;
    items[i % items.length].classList.toggle('blue');
}

var doc = document.getElementById('press');
doc.addEventListener('click',alternater);