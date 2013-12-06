var i = 0;
var items = document.querySelectorALL('li');
var alternater = function(e){    
    items[i % items.length].classlist.toggle('green');
    i++;
    items[i % items.length].classlist.toggle('green');
}

var doc = document.getElementById('press');
doc.addEventListener('click',alternater);