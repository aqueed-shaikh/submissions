var main = function(){
    var finished = document.getElementById("finish");
    var todo = document.getElementById("todo");

    var removeFromList = function(){
        finished.removeChild(this);
    }

    var isFinished = function(){
        finished.appendChild(this);
        this.addEventListener("click", removeFromList);
    }
    var move = function(){
        var item = document.getElementById("things");
        var input = item.value;
        var todoitem = document.createElement("li");
        todoitem.appendChild(document.createTextNode(input));
        todoitem.addEventListener("click",isFinished);
        todolist.appendChild(todoitem);
        item.value = "";
    }

    var sub = document.getElementById("submit");
    sub.addEventListener("click",move);
}();
