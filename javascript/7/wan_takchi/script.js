function changecolor(e){
    var a = document.getElementsByTagName("li");
    for(var x=0;x<a.length;x++){
        if(a[x].style.color === "blue"){
            a[x].style.color = "";
            a[x+1].style.color = blue;
            break;
        }
    }
}

document.getElementById("b1").addEventListener("click",changecolor);
