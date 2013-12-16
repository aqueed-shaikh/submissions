var todos = document.getElementById("todos");
var done = document.getElementById("done");
var submit = document.getElementById("submit");

var add = function() {
	var todo = document.getElementById("todo");
	var item = document.createElement("li");
	var text = document.createTextNode(todo.value);
	item.appendChild(text);
	todos.appendChild(item);
	item.addEventListener("click",finish);
	item.onmouseover=highlight;
	item.onmouseout=highlight;
	todo.value = "";
}

var finish = function () {
	done.appendChild(this);
	this.addEventListener("click",del);
}

var del = function() {
	done.removeChild(this);
}

var highlight = function() {
	this.classList.toggle('red');
}

submit.addEventListener("click",add);