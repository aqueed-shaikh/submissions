var FakeTodo = function() {
    var todoItems = document.getElementById('todo'),
        doneItems = document.getElementById('done'),
        input = document.getElementById('add_item'),
        syncDone = function(elt) {
            elt.addEventListener('click', function(e) {
                elt.remove();
            });
        },
        syncTodo = function(elt) {
            elt.addEventListener('click', function(e) {
                var newItem = document.createElement('li');
                newItem.innerText = this.innerText;
                syncDone(newItem);
                doneItems.appendChild(newItem);
                elt.remove();
            });
        };

    return {
        init: function() {
            input.addEventListener('keyup', function(e) {
                if(e.keyCode == 13) {
                    var newItem = document.createElement('li');
                    newItem.innerText = input.value;
                    input.value = '';
                    syncTodo(newItem);
                    todoItems.appendChild(newItem);
                }
            });
        }
    };
}();

FakeTodo.init();
