var main = function(){
    var finished = document.getElementById("finish");
    var todolist = document.getElementById("todo");

    var removeFromList = function(){
	finished.removeChild(this);
    }

    var movetofinish = function(){
	finished.appendChild(this);
	this.addEventListener("click", removeFromList);
    }

    var movetodo = function(){
	var text = document.getElementById("things");
	var input = text.value;
	var todoitem = document.createElement("li");
	todoitem.appendChild(document.createTextNode(input));
	todoitem.addEventListener("click",movetofinish);
	todolist.appendChild(todoitem);
	txtbx.value = "";
    }

    var submitbtn = document.getElementById("submit");
    submitbtn.addEventListener("click",movetodo);
}();
