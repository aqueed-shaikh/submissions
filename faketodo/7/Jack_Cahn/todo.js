var main = function() { 
    var submit = document.getElementById("add");
    var remove = function() { 
	document.getElementById("done").removeChild(this);}
    var movetodone = function() { 
	document.getElementById("done").appendChild(this);
	this.addEventListener('click', remove);}
    var move = function() { 
	x = document.getElementById("create");
	var newItem = document.createElement('li'); 
	var newNode = document.createTextNode(x.value); 
	newItem.appendChild(newNode); 
	newItem.addEventListener('click', movetodone); 
	document.querySelectorAll('ul')[0].appendChild(newItem); 
	x.value = ""; 
    }
    
    var submit = document.getElementById("add"); 
    submit.addEventListener("click", move);
    

}()
