var faketodo = function(){
    var todolist = document.getElementById("ToDo");
    var donelist = document.getElementById("Done");

    var addTask=function(){
	var tasks = document.getElementById("Task").value;
	var newItem = document.createElement("li");
	var newValue = document.createTextNode(tasks);
	newItem.appendChild(newValue);
	newItem.addEventListener("click",finishedTasks);
	todolist.appendChild(newItem);
    }
    
    var finishedTasks=function(){
	donelist.appendChild(this);
	this.addEventListener("click",deletefromDone);
    }

    var deletefromDone=function(){
	donelist.removeChild(this);
    }
    
    document.getElementById("Submit").addEventListener("click",addTask);
}();



