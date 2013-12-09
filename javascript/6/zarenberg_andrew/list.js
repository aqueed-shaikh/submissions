
col = "green";


function changeLi(e){
    var c = this.id == "liNext" ? 1 : -1;
    var a = document.getElementsByTagName("li");
    for(var x=0;x<a.length;x++){
	if(a[x].style.color == col){
	    a[x].style.color = "";
	    a[c==1?(x+1==a.length?0:x+1):(x==0?a.length-1:x-1)].style.color = col;
	    break;
	}
    }
}



document.getElementById("liNext").addEventListener("click",changeLi);
document.getElementById("liPrev").addEventListener("click",changeLi);
var a = document.getElementsByTagName("li");
for(var x=0;x<a.length;x++){
    a[x].addEventListener("mouseover",mouseOverLi).addEventListener("mouseout",mouseOutLi);
}
