var moveToDone = function(){
    var done = document.getElementById("done");
    var todo = document.getElementById("todo");
    done.appendChild(this);
    todo.removeChild(this);
}

var red = function(){
    this.classList.toggle('red');
}

var elts = document.querySelectorAll('li');
for(var i = 0; i < elts.length; i++){
    if elts[i].parentElement.id == "todo"{
	elts[i].addEventListener("click",red);
    }
}
