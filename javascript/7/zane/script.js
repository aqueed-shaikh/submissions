var e = document.createElement("h1");
e.innerHTML = "woop";
e.style.position = "absolute";
document.firstChild.appendChild(e);

var mover = function mover() {
	e.style.left = Math.random().toFixed(3) * 90 + "%";
	e.style.top = Math.random().toFixed(3) * 90 + "%";

	setTimeout(mover, 400);
}

mover();
