var $ = function(i) {
	return document.querySelectorAll(i); 
};

var clicks = 0;
$("#button")[0].addEventListener("click", function() {
	++clicks;
	document.getElementById("count").innerHTML=clicks;
});