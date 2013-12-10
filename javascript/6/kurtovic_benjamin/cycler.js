window.onload = function() {
    var button = document.getElementById("cycle");
    var i = 0;
    button.addEventListener("click", function() {
        var items = document.getElementsByClassName("item");
        items[i].classList.remove("highlighted");
        i = (i + 1) % items.length;
        items[i].classList.add("highlighted");
    });
}
