//js

var count=1;

var green=function(e) {
    this.classList.toggle('green');
}

var cat=document.getElementsByTagName('div');

var items=document.querySelectorAll('li');
items[0].classList.toggle('highlight');
var elt=document.getElementById('b1');
    elt.addEventListener('click',stepForward);



for (var i=0;i<cat.length;i++){
cat[i].addEventListener('mouseover',green);
cat[i].addEventListener('mouseout',green);
}

var stepForward=function(e){
    console.log(e);
    if (count-1<0){
	items[items.length-1].classList.toggle('highlight');}
    else{
	items[count-1].classList.toggle('highlight');}
    items[count].classList.toggle('highlight');
    count++;
    if (count>=items.length){
        count=0;
    }
}

var stepBackward=function(e){
    console.log(e);
    if (count-1<0){
	items[items.length-1].classList.toggle('highlight');
    }
    else{
    	items[count-1].classList.toggle('highlight');
    }
    if (count-2<-1){
	items[items.length-2].classList.toggle('highlight');
    }
    else if (count-2<0){
	items[items.length-1].classList.toggle('highlight');
    }
    else {
	items[count-2].classList.toggle('highlight');
    }
    count--;
    if (count<0){
        count=items.length-1;
    }
}


