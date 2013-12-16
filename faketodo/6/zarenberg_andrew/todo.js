/*
 * Andrew Zarenberg
 * Period 6
 */


document.getElementById("fm").addEventListener("submit",function(e){
    e.preventDefault ? e.preventDefault() : e.returnValue = false;


    var inp = document.getElementById("inp");

    // make sure there input is not blank
    if(inp.value.replace(/\s+/g,"") != ""){
	document.getElementById("todo_default").style.display = "none";
	var a = document.createElement("li");
	a.innerHTML = todoItem(inp.value);
	a.addEventListener("click",moveItem);
	document.getElementById("todo").appendChild(a);
	inp.value = "";
    } else {
	inp.value = "";
	alert("Error: Input cannot be left blank");
    }
});


function moveItem(e){

    if(this.parentNode.id == "todo"){
	var a = document.createElement("li");
	a.innerHTML = this.innerHTML+'<div class="done_time"><u>Completed:</u> '+(new Date()).toLocaleString()+'</div>'
	a.addEventListener("click",moveItem);
	document.getElementById("done").appendChild(a);
    }
    this.parentNode.removeChild(this);
	

    document.getElementById("todo_default").style.display = document.getElementById("todo").getElementsByTagName("li").length == 1 ? "" : "none";
    document.getElementById("done_default").style.display = document.getElementById("done").getElementsByTagName("li").length == 1 ? "" : "none";
}

function todoItem(n){
    return '<div class="todo_body">'+n+'</div><div class="todo_time"><u>Added:</u> '+(new Date()).toLocaleString()+'</div>'
}