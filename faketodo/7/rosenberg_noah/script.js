var moveToDone = function(){
    var done = document.getElementById("done");
    var todo = document.getElementById("todo");
    done.appendChild(this);
}

var newTodoItem = function(){
    console.log()
    var todo = document.getElementById('todo');
    var newItem = document.getElementById('newItem').value;
    if (newItem == "")
	return;
    var node = document.createTextNode(newItem);
    var li = document.createElement('li');
    li.appendChild(node);
    todo.appendChild(li);
    li.addEventListener('click',moveToDone);
    document.getElementById('newItem').value = "";    
}

var button = document.getElementById('b1');
button.addEventListener('click', newTodoItem);
