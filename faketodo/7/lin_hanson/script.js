var f = function(){
    var needed = document.getElementById("todo");
    var finished = document.getElementById("finished");

    var addTask = function(){
	var newTask = document.getElementById('task');
	var task = newTask.value;
	if(task !== ""){
	    var obj = document.createElement("li");
	    var change = document.createElement("input");
	    obj.appendChild(document.createTextNode(task));
	    
	    change.type = "submit";
	    change.value = "Delete Task";
	    change.addEventListener('click',swap);
	    obj.appendChild(change);	    	    
	    
	    obj.addEventListener('mouseover',highlight);
	    obj.addEventListener('mouseout',highlight);
	    obj.addEventListener('click',changeToDone);
	    needed.appendChild(obj);	    
	    newTask.value = "";
	}
    }

    var changeToDone = function(){
	finished.appendChild(this);
	this.removeEventListener('click',changeToDone);
	this.addEventListener('click',removeTask);
	this.querySelector('input').value = "Not done yet";
    }

    var changeToTodo = function(caller){
	needed.appendChild(caller);
	caller.removeEventListener('click',changeToTodo);
	caller.addEventListener('click',changeToDone);
	caller.querySelector('input').value = "Delete Task";
    }

    var swap = function(e){
	e.stopPropagation();
	if (this.value==="Delete Task")
	    this.parentElement.parentElement.removeChild(this.parentElement);
	else
	    changeToTodo(this.parentElement);
    }

    var removeTask = function(){
	this.parentElement.removeChild(this);
    }

    var highlight = function(){
	this.classList.toggle('highlight');
    }
           
    var button = document.getElementById('btn'); 
    button.addEventListener('click',addTask);
}()