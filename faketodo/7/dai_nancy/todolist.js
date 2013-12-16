var main = function(){
    var done = document.getElementById("done");
    var todo = document.getElementById("todo");
    
    var remove = function(){
	done.removeChild(this);
    }
    
    var complete = function(){
	this.addEventListener("click", remove);
	done.appendChild(this);
    }

    var add = function(){
	var text = document.getElementById("entry");
	var entry = text.value;
	text.value = "";
	var newI = document.createElement("li");
	newI.appendChild(document.createTextNode(entry));
	newI.addEventListener("click", complete);
	todo.appendChild(newI);
    }
    
    var submit = document.getElementById("submit");
    submit.addEventListener("click", add);
}();