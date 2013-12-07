var i = 0;
var list = document.querySelectorAll("li");	

var cycle = function(d){
    console.log(d);
    if(i == 0)
	list[i].classList.add("green");
    else{
	list[(i - 1) % list.length].classList.toggle("green");
	list[i % list.length].classList.toggle("green");
    } 
    i++;
	
}

var button = document.getElementById("c");
button.addEventListener("click", cycle);