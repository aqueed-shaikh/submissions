var main = function(){
    var donelist = document.getElementById("done");
    var todolist = document.getElementById("todo");
    
    var removeFromList = function(){
	donelist.removeChild(this);
    }
    var moveToDONE = function(){
	donelist.appendChild(this);
	this.addEventListener("click",removeFromList);
    }
    
    var moveToTODO = function(){
	var textbox = document.getElementById("whattodo");
	var input = textbox.value;
	var todoitem = document.createElement("li");
	todoitem.appendChild(document.createTextNode(input));
	todoitem.addEventListener("click",moveToDONE);
	todolist.appendChild(todoitem);
	textbox.value = "";
    }
    
    var submitbutton = document.getElementById("submit");
    submitbutton.addEventListener("click",moveToTODO);
}();
