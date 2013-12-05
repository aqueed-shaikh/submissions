var Orange = function(e) {
    e.classList.toggle('Orange');
}

var listItems = document.querySelectorAll('li');
var curIndex = 0;
var currentItem = listItems[curIndex];

function CycleUp() {
    Orange(currentItem);
    curIndex--;
    if(curIndex < 0) 
        curIndex = listItems.length - 1;
    currentItem = listItems[curIndex % listItems.length];
    Orange(currentItem);
    console.log("Hello");
}

function CycleDown() {
    Orange(currentItem);
    curIndex++;
    currentItem = listItems[curIndex % listItems.length];
    Orange(currentItem);
}