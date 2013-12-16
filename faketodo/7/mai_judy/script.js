//Judy Mai
//Softdev pd 7

var todostuff = document.getElementById("todo");
var donestuff = document.getElementById("done");

var finish = function(){
    donestuff.removeChild(this); //remove item from DONE
}

var moveDONE = function(){
    donestuff.appendChild(this); //add item to DONE
    this.addEventListener("click", finish); //if clicked, go to finish
}

var moveTODO = function(){
    var input = document.getElementById("input"); //grabs the textbox
    var todothing = input.value; //grabs input from textbox
    var item = document.createElement("li"); //create item element
    item.appendChild(document.createTextNode(todothing));
    item.addEventListener("click", moveDONE); //if clicked, move to DONE
    todostuff.appendChild(item); 
    input.value = ""; //set back to default
}

var submit = document.getElementById("submit");
submit.addEventListener("click", moveTODO); //if submit, move to TODO