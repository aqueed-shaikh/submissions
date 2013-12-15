var main = function(){
    var finished = document.getElementById("finish");
    var todo = document.getElementById("todo");

    var removeFromList = function(){
        finished.removeChild(this);
    }

    var isFinished = function(){
        finished.appendChild(this);
        this.addEventListener("click", removeFromList);
    }

  }();
