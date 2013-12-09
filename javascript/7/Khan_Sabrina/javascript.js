var blue=function(e){
    console.log(e);
    this.classList.toggle("blue");
}

var a=0;

var blue=function(e){
    console.log(e);
    var things = document.querySelectorAll("li");
    things[a%things.length].classList.toggle("blue");
    things[(a+1)%things.length].classList.toggle("blue");
    a++;    
}

var things = document.querySelectorAll("li");
things[0].classList.add("blue");
var button=document.getElementById("b1");
button.addEventListener("click",blue);
