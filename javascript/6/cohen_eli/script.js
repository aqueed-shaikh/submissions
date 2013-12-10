var pos = 8;

var cl = ['red','green','blue','yellow','pink','brown','orange','tur'];

var down = function(e){

    var items = document.querySelectorAll("li");

    if (pos == 8 || pos == -1){
	pos = 0;
    }
    
    else{

	
	items[pos].classList.toggle(cl[pos]);
    
	pos++;
    }
    
    if (pos < 8)
	items[pos].classList.toggle(cl[pos]);
}


var up = function(e){

    var items = document.querySelectorAll("li");

    if (pos == -1 || pos == 8){
	pos = 7;
    }
    
    else{

	
	items[pos].classList.toggle(cl[pos]);
    
	pos--;
    }
    
    if (pos > -1)
	items[pos].classList.toggle(cl[pos]);
}



var bdown = document.getElementById('bdown');
bdown.addEventListener('click', down);

var bup = document.getElementById('bup');
bup.addEventListener('click', up);