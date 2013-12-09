var i = 0;

var cycling = function(li){
    var li = document.getElementsByTagName('li')
    console.log(i);
    if(i < li.length - 1){
	li[i++].classList.remove('green');
	li[i].classList.add('green');
    }
    else{
	li[i].classList.remove('green');
	i=0;
	li[i].classList.add('green');
    }
}



var elts = document.getElementById('cycle')
elts.addEventListener('click',cycling);