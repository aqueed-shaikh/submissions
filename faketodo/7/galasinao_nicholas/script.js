
var list = function(){
    var notdone = document.getElementById("notdone");
    var done = document.getElementById("done");

    var remove = function(){
	done.removeChild(this);
    }

    var done = function(){
	this.addEventListener("click", remove);
	done.appendChild(this);
    }

    var notdone = function(){
	var input = document.getElementById("task");
	var text = input.value;
	var item = document.createElement("li");
	item.appendChild(document.createTextNode(text));
	item.addEventListener("click", done);
	notdone.appendChild(item);
	input.value = "";
    }

    var submit = document.getElementById("submit");
    submit.addEventListener("click", notdone);
}();