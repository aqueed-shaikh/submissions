var list = document.querySelectorAll("li");
var currItem = 0;

var cycledown = function (){
    list[currItem].classList.remove("colored");
    currItem++;
    if(currItem == list.length)
        currItem %= list.length;
    list[currItem].classList.add("colored");
}

var cycleup = function (){
    list[currItem].classList.remove("colored");
    currItem--;
    if(currItem == -1)
        currItem = list.length - 1;
    list[currItem].classList.add("colored");
}

var cycleDown = document.getElementById("buttondown");
var cycleUp = document.getElementById("buttonup");
cycleDown.addEventListener("click", cycledown);
cycleUp.addEventListener("click", cycleup);
