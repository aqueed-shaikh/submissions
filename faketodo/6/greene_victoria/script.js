function add() {
    var num = document.getElementById ("new").value;
    var item = document.createElement ("li");
    var name = document.createTextNode (num);
    item.appendChild (name);
    item.addEventListener ('click',done);    
    var list = document.getElementById ('todolist');
    list.appendChild (item);
    var num = document.getElementById ("new").value = "";
}

function done() {
    var list = document.getElementById ('todolist');
    list.removeChild (this); 
    var doneitems = document.getElementById ("donelist");
    doneitems.appendChild (this);
    this.addEventListener ('click', remove);
}

function remove() {
    var donelist = document.getElementById ("donelist");
    donelist.removeChild (this);
}