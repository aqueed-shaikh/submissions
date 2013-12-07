	var start = 0
	
	var pink = function (e){
		console.log(e);
		this.classList.toggle('pink');

}

	var purple = function(e) {
		console.log(e);
		this.classList.toggle('purple');
		
}

	var change = function (e){
	console.log(e);
	var items = document.querySelectorAll('li');
	for (var i = 0; i < items.length; i++) {
            items[i].classList.toggle('pink');
        }
	}
}

	var button = document.getElementById('b1);
	button.addEventListener('click',change);


//not done, will complete soon.
	