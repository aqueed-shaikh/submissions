var lists = document.querySelectorAll('ul');
var todo = lists[0];
var done = lists[1];
var button = document.getElementById("submit");
var box = document.getElementById("new");


var deleteItem = function(e) {
    done.removeChild(this);
}

var itemDone = function(e) {
    todo.removeChild(this);
    done.appendChild(this);
    this.removeEventListener('click',itemDone);
    this.addEventListener('click',deleteItem);
}


var newItem = function(e) {
    var newli = document.createElement('li');
    var t = document.createTextNode(box.value);
    newli.appendChild(t);
    todo.appendChild(newli);
    newli.addEventListener('click',itemDone);
}


button.addEventListener("click", newItem, false);


