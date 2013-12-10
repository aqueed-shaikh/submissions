var num = document.getElementById('Cycle Num');
var color = document.getElementById('Cycle Color');


var red = function(e){
    this.classList.toggle('red');
}

var redback = function(e){
    this.classList.toggle('redback');
}

var green = function(e){
    this.classList.toggle('green');
}

var greenback = function(e){
    this.classList.toggle('greenback');
}

var blue = function(e){
    this.classList.toggle('blue');
}

var blueback = function(e){
    this.classList.toggle('blueback');
}

/*
for (var i = 0; i<elts.length; i++){
    elts[i].addEventListener('mousedown',red);
    elts[i].addEventListener('mouseup',red);   
    elts[i].addEventListener('mouseover',blueback);
    elts[i].addEventListener('mouseout',blueback);
    elts[i].addEventListener('dblclick',green);  
}
*/


var items = document.querySelectorAll('li');
var i = 0;
var c = 0;
var colors = ['red','blue','green'];
var col = colors[c];
    
var cycleNum = function(){
    if (i >= items.length-1 ){
	items[i].classList.remove(col);
	i=0;
	items[i].classList.add(col);
	console.log(i);
    }
    else{
	items[i].classList.remove(col);
	i++;
	items[i].classList.add(col);
	console.log(i);
    }
}


var cycleCol = function(){
    items[i].classList.remove(col);
    if (c >= colors.length-1 ){ c = 0; }
    else{ c++; }
    col=colors[c];
    items[i].classList.add(col);
    console.log(col);
}

num.addEventListener('click',cycleNum);
color.addEventListener('click',cycleCol);