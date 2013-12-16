var todo, done;

function create_new(input) {
    var li = document.createElement("li");
    var text = document.createTextNode(input);
    li.appendChild(text);
    li.addEventListener("click", function() {
        if (this.parentNode == todo) {
            todo.removeChild(this);
            done.appendChild(this);
        }
        else
            done.removeChild(this);
    });
    todo.appendChild(li);
}

window.onload = function() {
    todo = document.getElementById("todo");
    done = document.getElementById("done");
    var button = document.getElementById("submit");
    button.addEventListener("click", function() {
        var input = document.getElementById("input");
        if (input.value != "") {
            create_new(input.value);
            input.value = "";
        }
    });
}
