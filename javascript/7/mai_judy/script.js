//Judy Mai
//Softdev pd 7

var i = -1; //starter point (blank)

var elts = document.querySelectorAll('li');

var next = function(e){
  //untoggle previous
	if (i > -1)
		elts[i].classList.toggle('red');

	//update current + loop if necessary
	i++; 
	if (i == elts.length) 
		i = 0; 

	//toggle current
	elts[i].classList.toggle('red'); 
}


var back = function(e){
	//untoggle previous
	if (i > -1)
		elts[i].classList.toggle('red'); 

	//update current + loop if necessary
	if (i == -1) 
		i++; //account for initial back
	i--;
	if (i == -1) 
	i = elts.length-1; 

	//toggle current
	elts[i].classList.toggle('red'); 
}


var reset = function(e){
	if (i != -1)
		elts[i].classList.toggle('red');
	i = -1;
}


//create buttons that goes next/back/reset each click
var elt=document.getElementById('b1');
elt.addEventListener('click',next);
var elt2=document.getElementById('b2');
elt2.addEventListener('click',back);
var elt3=document.getElementById('b3');
elt3.addEventListener('click',reset);
