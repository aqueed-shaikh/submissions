function changecolor(e){
    var items = document.getElementsByTagName("li");
    for(var x=0;x<items.length;x++){
        if(items[x].style.color === "blue"){
            items[x].style.color = "";
            if(x+1===items.length){
                items[0].style.color="blue";
            }
            else{
                items[x+1].style.color = "blue";
            break;
            }
        }
    }
}

document.getElementById("b1").addEventListener("click",changecolor);
