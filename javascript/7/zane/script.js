var GAME = {

	interval : 2000,
	intervalDiff : 50,
	count : 0

}

var setup = function() {

	var b = document.createElement("button");
	b.innerHTML = "for the lulz";
	b.style.position = "absolute";
	b.style.left = "45%";
	b.style.top  = "45%";
	b.addEventListener("click", firstClick);
	document.firstChild.appendChild(b);

	var points = document.createElement("div");
	points.id = "points";
	document.firstChild.appendChild(points);

	GAME.b = b;
}

var main = function() {

	moveAll();
	setTimeout(main, GAME.interval);
}

var moveAll = function() {

	move(GAME.b);
	var points = document.getElementById("points").children;
	for (var i=0; i<points.length; i++) {
		move(points[i]);
	}
}

var move = function(element) {

	element.style.left = Math.random().toFixed(3) * 90 + "%";
	element.style.top = Math.random().toFixed(3) * 90 + "%";
}

var score = function() {

	var points = document.getElementById("points");
	if (points.children.length > 0)
		points.children[GAME.count-1].style.color = "black";

	GAME.count++;

	var e = document.createElement("h1");
	e.innerHTML = GAME.count;
	e.style.color = "red";
	e.style.position = "absolute";
	document.getElementById("points").appendChild(e);

	GAME.interval -= GAME.intervalDiff;

	moveAll();
}

var firstClick = function() {

	var b = GAME.b;
	b.removeEventListener('click', firstClick);
	b.addEventListener('click', score);
	score();
	main();
}

setup();
