var elts = document.querySelectorAll('li');

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

for (var i = 0; i<elts.length; i++){
    elts[i].addEventListener('mousedown',red);
    elts[i].addEventListener('mouseup',red);   
    elts[i].addEventListener('mouseover',blueback);
    elts[i].addEventListener('mouseout',blueback);
    elts[i].addEventListener('dblclick',green);
}