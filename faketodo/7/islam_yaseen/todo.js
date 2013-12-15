var toDoApp=function(){
    //document.getElementById("button").onclick=f1;
    return{
	f1:function(){
	    var tempNode=document.createElement("LI");
	    var tempText=document.getElementById("input").value;
	    var tempTextNode=document.createTextNode(tempText);
	    tempNode.appendChild(tempTextNode);
	    tempNode.onclick=toDoApp.f2;
	    document.getElementById("todo").appendChild(tempNode);
	},
	/*f3:function(){
	    document.getElementById("button").onclick=this.f1;
	}(),*/
	f2:function(){
	    var tempNode=document.createElement("LI");
	    var tempText=this.innerHTML;
	    var tempTextNode=document.createTextNode(tempText);
	    tempNode.appendChild(tempTextNode);
	    tempNode.onclick=function(){
		this.classList.toggle("redback");
		this.parentNode.removeChild(this);
	    };
	    document.getElementById("done").appendChild(tempNode);
	    this.classList.toggle("redback");
	    this.parentNode.removeChild(this);
	}
    }
}()

document.getElementById("button").onclick=toDoApp.f1;
