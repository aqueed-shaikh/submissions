var activeList = -1

var green = function(e){
    this.classList.toggle('green');
}

var cycle = function(e) {
    var elts = document.querySelectorAll('li');
    if (activeList > -1){
	elts[activeList].classList.toggle('green');
    }
    activeList++;
    if (activeList == elts.length){
	activeList = 0;
    }
    elts[activeList].classList.toggle('green'); 
}

var cycleB = function(e) {
    var elts = document.querySelectorAll('li');
    if (activeList > -1)
	elts[activeList].classList.toggle('green');
    activeList--;
    if (activeList < 0){
	activeList = elts.length-1;
    }
    elts[activeList].classList.toggle('green');
}
