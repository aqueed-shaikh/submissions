var fancifyMe = document.querySelectorAll('li');

var fancify = function() {
    for (var i = 0; i < fancifyMe.length; i++){
        fancifyMe[i].classList.add('fancy');
    }
}

document.getElementById("f").addEventListener("click",fancify);
