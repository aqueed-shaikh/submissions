var drop = function(){
	var node = document.createElement("li");
	var input = document.getElementById("input").value;
	if (input != "") {
		node.innerHTML = input;
		node.addEventListener("click", notdone);
		document.getElementById("notdone").appendChild(node);
	}
}

var notdone = function(){
	this.addEventListener("click",done);
	document.getElementById("done").appendChild(this);
	document.getElementById("notdone").removeChild(this);
}

var done = function(){
	document.getElementById("done").removeChild(this);
}
