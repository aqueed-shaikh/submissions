var $ = function(i) {
	return document.querySelectorAll(i); 
};

var list = $("li");
var prev = 0, cur = 0;
$("#button")[0].addEventListener("click", function() {
	list[prev].className = "";
	list[cur].className = "change";
	prev = cur;
	cur = (cur + 1) % list.length;
});