var global = {
	cycleElement : "li",
	buttonID : "cycle"
};

var listItems = document.querySelectorAll("li");
var currItem = 0;

var cycle = function (){
	listItems[currItem].classList.remove("colored");
	currItem++;
	if(currItem == listItems.length)
		currItem %= listItems.length;
	listItems[currItem].classList.add("colored");
}

var cycleButton = document.getElementById("cycle");
cycleButton.addEventListener("click", cycle);
