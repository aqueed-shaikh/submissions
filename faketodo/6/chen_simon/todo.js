var button = document.getElementById("submit");
button.addEventListener("click",add);

function add(e){
    var todo = document.getElementById("input").value;
    var li = document.createElement("li");
    li.innerHTML = todo;
    li.addEventListener("click",done);
    var todolist = document.getElementById("todo");
    todolist.appendChild(li);

}

function done(e){
    var done = document.getElementById("todo").removeChild(this);
    document.getElementById("done").appendChild(this);
    this.addEventListener("click",remove);
}

function remove(e){
    document.getElementById("done").removeChild(this);
}