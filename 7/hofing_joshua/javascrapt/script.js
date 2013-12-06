var curr1 = 0;
var curr2 = 0;
var crueltyConst = 10;

function doThings() {
    var list = document.querySelectorAll("li");
    list[curr1].style.color = "";
    curr1++;
    curr1 %= list.length;
    list[curr1].style.color = "red";
    setTimeout(doThings, 300);
}

function doOtherThings() {
    var list = document.querySelectorAll("li");
    list[curr2].style.backgroundColor = "";
    curr2++;
    curr2 %= list.length;
    list[curr2].style.backgroundColor = "blue";
    setTimeout(doOtherThings, 300 + crueltyConst);

}


doThings();
doOtherThings();
