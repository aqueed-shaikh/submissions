var blue = function(e){
    this.classList.toggle('blue');
}

    var purple = function(e){
	this.classList.toggle('purple');
    }


	var button1 = function(e){
	    var elts = document.querySelectorAll('li');
	    for (var i = 0; i < elts.length;i++){
		if (i%2==0){
		    elts[i].classList.toggle('blue');
		    elts[i].addEventListener('click',green);
		}
	    }
	}

	    var button2 = function(e){
		var elts = document.querySelectorAll('li');
		for (var i = 0; i < elts.length;i++){
		    if (i%2!=0){
			elts[i].classList.toggle('red');
			elts[i].addEventListener('click',purple);
		    }
		}
	    }
