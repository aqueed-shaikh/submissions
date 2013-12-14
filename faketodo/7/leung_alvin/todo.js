var removeFromList = function(){
    document.getElementById("done").removeChild(this);
}
var moveToDONE = function(){
    var donelist = document.getElementById("done");
    donelist.appendChild(this);
    this.addEventListener("click",removeFromList);
}

var moveToTODO = function(){
    var textbox = document.getElementById("whattodo");
    var input = textbox.value;
    var todolist = document.getElementById("todo");
    var todoitem = document.createElement("li");
    todoitem.appendChild(document.createTextNode(input));
    todoitem.addEventListener("click",moveToDONE);
    todolist.appendChild(todoitem);
    textbox.value = "";
}

var submitbutton = document.getElementById("submit");
submitbutton.addEventListener("click",moveToTODO);

