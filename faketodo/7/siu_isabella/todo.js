var main = function(){
    var finlist = document.getElementById("fin");
    var todolist = document.getElementById("todo");

    var removeFromList = function(){
	finlist.removeChild(this);
    }

    var moveToFin = function(){
	finlist.appendChild(this);
	this.addEventListener("click", removeFromList);
    }

    var moveToToDo = function(){
	var txtbx = document.getElementById("stuff");
	var input = txtbx.value;
	var todoitem = document.createElement("li");
	todoitem.appendChild(document.createTextNode(input));
	todoitem.addEventListener("click",moveToFin);
	todolist.appendChild(todoitem);
	txtbx.value = "";
    }

    var submitbtn = document.getElementById("submit");
    submitbtn.addEventListener("click",moveToToDo);
}();
