var character = document.getElementById("character");
var block = document.getElementById("block");

function jump(){
    if(character.classList != "animate"){
    character.classList.add("animate");
    }
    setTimeout(function(){
        character.classList.remove("animate");
    },500);
}

document.onkeydown = (e) => {
    e = e || window.event;
    //Up arrow
    if (e.keyCode === 38) {
        jump();
    }
    //space
    if (e.keyCode === 32) {
        jump();
    }    
    //w
    if (e.keyCode === 87) {
        jump();
    }  
}

var checkDead = setInterval(function(){
    var characterTop = parseInt(window.getComputedStyle(character).getPropertyValue("top"));
    var blockLeft = parseInt(window.getComputedStyle(block).getPropertyValue("left"));
    if(blockLeft<20 && blockLeft>0 && characterTop>=130){
        block.style.animation = "none";
        block.style.display = "none";
        alert("Game Over")
    }
},10);