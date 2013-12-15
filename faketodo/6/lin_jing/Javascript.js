function addItem()
{
    var toBeAdded = document.getElementById("text").value;
    var Item = document.createElement("li");
    Item.innerHTML = toBeAdded;
    Item.addEventListener("click", PopToDone);
    document.getElementById("todo").appendChild(Item);
}

function PopToDone() 
{
    var Item = document.getElementById("todo");
    document.getElementById("done").appendChild(Item);
    this.removeEventListener("click", PopToDone);
    this.addEventListener("click", Delete);
}

function Delete() 
{
    document.getElementById("done").removeChild(this);
}