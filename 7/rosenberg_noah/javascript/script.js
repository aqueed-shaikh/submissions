
var red = function (e){
    console.log(e);
    this.classList.toggle('red');

}

var a = 0;
var green = function (e){
    console.log(e);
    var elts = document.querySelectorAll('li');
    elts[a%elts.length].classList.toggle('green');
    elts[(a+1)%elts.length].classList.toggle('green');
    a ++;
}




var elts = document.querySelectorAll('li');
elts[0].classList.add('green');
var button = document.getElementById('b1');
//    elts[i].addEventListener('mouseover',red);
  //  elts[i].addEventListener('mouseout',red);
button.addEventListener('click',green);
