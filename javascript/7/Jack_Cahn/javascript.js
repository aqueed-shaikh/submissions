function move(e){
    var myStuff = document.getElementsByTagName("li");
    for(var listItem = 0; listItem < myStuff.length; listItem++) {
        if(myStuff[listItem].style.color == "red"){
            myStuff[listItem].style.color = "purple";
            if( listItem + 1 == myStuff.length ){ myStuff[0].style.color="red"}
            else{myStuff[listItem+1].style.color = "red";break;}
        }}}
document.getElementById("clicked").addEventListener("click", move);

   
