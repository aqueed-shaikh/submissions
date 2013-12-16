var add = function(e){
    var input = document.getElementById('in');
    var text = input.value;

    if(text != ""){
	var newnode = document.createElement("li");
	var newtext = document.createTextNode(text);
	newnode.appendChild(newtext);
	newnode.addEventListener('click',done); 
	document.getElementById("todo").appendChild(newnode);
	input.value = "";
    }
}

var done = function(e){
 
    document.getElementById("todo").removeChild(this);
    document.getElementById("done").appendChild(this);
    this.removeEventListener('click',done);
    this.addEventListener('click',kill);
}

var kill = function(e){
    var item = this;
   
    document.getElementById("done").removeChild(this);
}

var sub = document.getElementById('submit');
sub.addEventListener('click', add);

