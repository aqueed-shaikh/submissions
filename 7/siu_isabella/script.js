var n = 0;

var blue = function(e){
    console.log(e);
    var items = document.querySelectorAll('li');
    items[n%items.length].classList.toggle('blue');
    items[(n+1)%items.length].classList.toggle('blue');
    n++;
}

var a = document.getElementById('btn');
a.addEventListener('click',blue)
