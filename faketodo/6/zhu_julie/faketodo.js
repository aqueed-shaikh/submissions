var todo = document.getElementById("todo");
var done = document.getElementById("done");

var add = function(e){
    var text = document.getElementById("input").value;
    var li = document.createElement("li");
    var value = document.createTextNode(text);
    li.appendChild(value);
    document.getElementById("input").value="";
    li.addEventListener("click",finished);
    todo.appendChild(li);
}

var button = document.getElementById("button1");
button.addEventListener("click",add);

var finished = function(e){
    todo.removeChild(this);
    done.appendChild(this);
    this.addEventListener("click",remove);
}

var remove = function(e){
    done.removeChild(this);
}
