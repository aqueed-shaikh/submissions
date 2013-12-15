
var green = function(e){
    this.classList.toggle('green');
}
var red = function(e){
    this.classList.toggle('red');
}

var addtodo = function(e){
    var dork = document.getElementById("stuff");
    if(dork.value != ""){
	var mork =  document.getElementById("todo");
	mork.innerHTML = mork.innerHTML + "<li class="+"todo"+">" + dork.value + "</li>";
	dork.value = "";
	var toit = document.querySelectorAll('li.todo');
	for(var i = 0; i < toit.length;i++){
	    toit[i].addEventListener('click', change);
	    toit[i].addEventListener('mouseover', green);
	    toit[i].addEventListener('mouseout', green);
	}
    }
}

var remo = function(e){
    this.parentNode.removeChild(this);
}

function addone(thus){
    var mork =  document.getElementById("done");
    mork.appendChild(thus)
    thus.addEventListener('click', remo);
    //thus.addEventListener('mouseover', red);
    //thus.addEventListener('mouseout', red);
}

var change = function(e){
    this.parentNode.removeChild(this);
    addone(this);
}
    

document.getElementById("butt").addEventListener('click', addtodo);