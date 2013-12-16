var movedown = function(){
	this.addEventListener('click',disappear);
	document.getElementById("dead").appendChild(this);
	document.getElementById("alive").removeChild(this);
}

var disappear = function(){
	document.getElementById("dead").removeChild(this);
}


var add = function(){
	var node = document.createElement("li");
	var input = document.getElementById("text").value;
	node.innerHTML = input;
	node.addEventListener("click", movedown);
	document.getElementById("alive").appendChild(node);
}
