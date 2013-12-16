var eniv = function(){
    var todos = document.getElementById("todo");
    var dones = document.getElementById("done");

    var addTask = function(){
	var newTask = document.getElementById('task');
	var task = newTask.value;
	if(task !== ""){
	    var item = document.createElement("li");
	    var alt = document.createElement("input");
	    item.appendChild(document.createTextNode(task));
	    
	    alt.type = "submit";
	    alt.value = "Delete Task";
	    alt.addEventListener('click',altFxn);
	    item.appendChild(alt);	    	    
	    
	    item.addEventListener('mouseover',highlight);
	    item.addEventListener('mouseout',highlight);
	    item.addEventListener('click',changeToDone);
	    todos.appendChild(item);	    
	    newTask.value = "";
	}
    }

    var changeToDone = function(){
	dones.appendChild(this);
	this.removeEventListener('click',changeToDone);
	this.addEventListener('click',removeTask);
	this.querySelector('input').value = "Not done yet";
    }

    var changeToTodo = function(caller){
	todos.appendChild(caller);
	caller.removeEventListener('click',changeToTodo);
	caller.addEventListener('click',changeToDone);
	caller.querySelector('input').value = "Delete Task";
    }

    var altFxn = function(e){
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