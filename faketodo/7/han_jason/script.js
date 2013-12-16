var main = function() {

    var todo = document.getElementById("a");
    var done = document.getElementById("b");

    var kill = function() {
	done.removeChild(this);
    }

    var move = function() {
	done.appendChild(this);
	this.addEventListener("click", kill);
    }

    var add = function() {
	var i = document.getElementById("i");
	var x = i.value;
	var j = document.createElement("li");
	j.appendChild(document.createTextNode(x));
	j.addEventListener("click", move);
	todo.appendChild(j);
	i.value = "";
    }

    var b = document.getElementById("s");
    b.addEventListener("click", add);

}();
