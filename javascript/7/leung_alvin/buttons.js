var placeholder = 0;
var next = function(e){
    var lis = document.getElementsByTagName('li');
    lis[placeholder++ % lis.length].classList.toggle('green');
    lis[placeholder % lis.length].classList.toggle('green');
}
var wai = function(e){
    alert("WHY DID YOU PRESS THE BUTTON??");
    var lis = document.getElementsByTagName('li');
    for(var i = 0;i < lis.length;i++){
	lis[i].classList.toggle('bad');
    }
}

document.getElementById('press').addEventListener('click',next);
document.getElementById('dontpress').addEventListener('click',wai);

