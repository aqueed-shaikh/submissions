var dofunk = function() {
    return {
	add:function(e) {
	    var item = document.getElementById('indo');
	    if (item.value == "") {
		alert('Enter a do!');
		return;
	    }
	    var li = document.createElement('li');
	    li.textContent = item.value;
	    li.addEventListener('click', this.remove);
	    var todo = document.getElementById('todo');
	    todo.appendChild(li);
	    item.value = "";
	},
	remove:function(e) {
	    var todone = document.getElementById('todone');
	    todone.appendChild(e.target);
	}
    }
}()

