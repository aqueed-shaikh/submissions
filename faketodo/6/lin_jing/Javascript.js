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
    
    this.removeEventListener("click", PopToDone);
    this.addEventListener("click", Delete);
    document.getElementById("done").appendChild(this);

}

function Delete() 
{
    document.getElementById("done").removeChild(this);
}