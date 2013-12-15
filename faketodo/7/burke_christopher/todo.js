var closure = function(){
    var newItem = function(){};
    var deleteItem = function(){};
    var backToTodo = function(){};
    var undo = function(){};
    var itemDone = function(){};
    var submitItem = function(){};

    var lists = document.querySelectorAll('ul');
    var todo = lists[0];
    var done = lists[1];
    var button1 = document.getElementById("add");
    var button2 = document.getElementById("undo");
    var box = document.getElementById("new");
    
    
    var deleteItem = function(e) {
	done.removeChild(this);
    }
    
    
    var newItem = function(e) {
	if (box.value === "") {
	    return;
	}
	var newli = document.createElement('li');
	var t = document.createTextNode(box.value);
	newli.appendChild(t);
	todo.appendChild(newli);
	newli.addEventListener('click',itemDone);
	box.value = "";
    }

    var backToTodo = function(e) {
	done.removeChild(this);
	todo.appendChild(this);
	this.removeEventListener("click",backToTodo);
	this.addEventListener("click",itemDone);
    }

    var undo = function(e) {
	var listItems = done.childNodes;
	done.classList.toggle('blue');
	done.classList.toggle('red');
	if (done.classList.contains('red')) {
	    for(var i = 0; i < listItems.length; i++) {
		listItems[i].addEventListener("click",backToTodo);
		listItems[i].removeEventListener('click',deleteItem);
	    }
	} else {
	    for(var i = 0; i < listItems.length; i++) {
		listItems[i].addEventListener("click",deleteItem);
		listItems[i].removeEventListener("click",backToTodo);
	    }
	}
    }
    
    var itemDone = function(e) {
	todo.removeChild(this);
	done.appendChild(this);
	this.removeEventListener('click',itemDone);
	if(done.classList.contains('red')) {
	    this.addEventListener("click",backToTodo);
	} else {
	    this.addEventListener('click',deleteItem);
	}
    }

    var submitItem = function(e) {
	if(e.keyIdentifier === "Enter") {
	    newItem(e);
	}
    }

    button1.addEventListener("click", newItem, false);
    button2.addEventListener("click", undo, false);
    box.addEventListener("keypress", submitItem, false);
}()

