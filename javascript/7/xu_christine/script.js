
	var start = 0;
	
	var pink = function (e){
		console.log(e);
		var items = document.querySelectorAll('li');
		this.classList.toggle("pink");
}
	var purple = function(e) {
		console.log(e);
		this.classList.toggle("purple");
}

	var change () = function(e){
		console.log(e);
		var items = document.querySelectorAll('li');
		items[start%items.length].classList.toggle("pink")
		items[(start++)%items.length()].classList.toggle("purple");
        }
	

	var push = document.getElementById('b1);
	push.addEventListener('click',change);
