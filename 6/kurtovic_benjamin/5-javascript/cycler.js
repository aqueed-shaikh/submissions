window.onload = function() {
    var button = document.getElementById("cycle");
    var i = 0;
    button.addEventListener("click", function() {
        var items = document.getElementsByClassName("item");
        items[i].classList.remove("highlighted");
        i++;
        if (i >= items.length)
            i = 0;
        items[i].classList.add("highlighted");
    });
}
