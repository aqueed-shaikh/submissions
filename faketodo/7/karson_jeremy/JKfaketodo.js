//thanks to sweyn for showing me how to get value from the text <input>

//thanks to maia for suggesting I add the new event listener in a different 
//function... before that it WOULD NOT WORK!

var listElement;

var makeToDoElement = function(){
    var textField = document.getElementById('thingtodo');
    var textValue = textField.value;
    if (textValue != ""){
	listElement = document.createElement("li");
	listElement.appendChild(document.createTextNode(textValue));
	todolist.appendChild(listElement);
	listElement.addEventListener('click', switchToDoneList);
	listElement.addEventListener('mouseover', blue);
	listElement.addEventListener('mouseout', blue);
    }
}

var blue = function(){
    this.classList.toggle('blue');
}

var switchToDoneList = function(){
    listElement = this;
    donelist.appendChild(listElement);
    listElement.addEventListener('click', remove);
}

var remove = function(){
    listElement = this;
    donelist.removeChild(listElement);
}


var button = document.getElementById('submit');
button.addEventListener('click', makeToDoElement);
var todolist = document.getElementById('todolist');
var donelist = document.getElementById('donelist');