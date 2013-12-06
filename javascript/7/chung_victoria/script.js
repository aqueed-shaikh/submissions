var redback = function(e) {
//    this.classList.toggle('red');
    e.classList.toggle('red')
    e.classList.toggle('grow')
}

var changeFont = function (e){
    e.style.fontSize = "30px";
}

var revertFont = function(e) {
    e.style.fontSize="";
}

var green = function(e) {
    this.classList.toggle('green');
}

var red = function(e) {
    console.log(e);
    var items = document.querySelectorAll('li');
    for (var i = 0; i < items.length; i++) {
        items[i].classList.toggle('red');
    }
}

var stripe = function(e) {
    console.log(e);
    var items = document.querySelectorAll('li');
    for (var i = 0; i < items.length; i++) {
        if (i % 2 == 0) {
            items[i].classList.add('red');
        }
        else {
            items[i].classList.add('blue');
        }
    }
}
