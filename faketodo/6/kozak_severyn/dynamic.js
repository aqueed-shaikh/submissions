var addTaskButton = document.getElementById("addTask");

var removeTask = function(){
	this.remove();
};

var moveTask = function(){
	this.remove();
	document.getElementById("done").appendChild(this);
	this.addEventListener("click", removeTask);
};

addTaskButton.addEventListener("click", function(){
	var taskText = document.getElementById("task").value;
	var newTask = document.createElement("li");
	newTask.appendChild(document.createTextNode(taskText));
	newTask.addEventListener("click", moveTask);
	document.getElementById("toDo").appendChild(newTask);
});
