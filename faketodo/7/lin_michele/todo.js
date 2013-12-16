var main = function(){

    var todo = document.getElementById("todo");
    var todone = document.getElementById("todone");

    var remove = function(){
	todone.removeChild(this);
    }

    var move = function(){
	todone.appendChild(this);
	this.addEventListener("click", remove);
    }

    var add = function(){
	var enter = document.getElementById("newtodo");
	var input = enter.value;
	var newtodo = document.createElement("li");
	newtodo.appendChild(document.createTextNode(input));
	newtodo.addEventListener("click",move);
	todo.appendChild(newtodo);
	enter.value= "";
    }

    var submit = document.getElementById("submit");
    submit.addEventListener("click", add);
}();
  

