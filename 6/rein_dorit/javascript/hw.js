var green = function(q){
    q.classList.toggle('green');
}

var elements = document.querySelectorAll('li');
var index = 0;
var thisItem = elements[index];
var length = elements.length - 1;

function colChange(){
    if(index < 0)
	index = length;
    thisItem = elements[index]
    green(thisItem);
    index--;
    console.log("tester");
}

function colBack(){
    if (index > length)
	index = 0;
    thisItem = elements[index]
    green(thisItem);
    index++;
    console.log("newtest")
}
