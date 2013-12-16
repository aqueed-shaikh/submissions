var button = document.getElementById("submit");
var input = document.getElementById("item");
var todolist = document.getElementById("todo");
var done = document.getElementById("done");

var newItem = function(){
    var newList = document.createElement('li');
    var text = document.createTextNode(input.value);
    newList.appendChild(text);
    console.log(newList);
    todolist.appendChild(newList);
    newList.addEventListener('click', addDone);
    input.value = "";
}

var addDone = function(){
    done.appendChild(this);
    this.removeEventListener('click', addDone);
    this.addEventListener('click', remove);
}

var remove = function(){
    done.removeChild(this);
}

button.addEventListener('click', newItem);
