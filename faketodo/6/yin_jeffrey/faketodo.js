var markComplete = function(){
    document.getElementById("todo").removeChild(this);
    this.removeEventListener("click",addItem)
    document.getElementById("done").appendChild(this);    
}
var addItem= function(){
    console.log("hello");
    x=document.getElementById("input").value;
    document.getElementById("input").value="";
    console.log(x);
    item = document.createElement("li");
    item.appendChild(document.createTextNode(x));
    item.addEventListener("click",markComplete)
    document.getElementById("todo").appendChild(item);
}

document.getElementById("addItem").addEventListener("click",addItem);
