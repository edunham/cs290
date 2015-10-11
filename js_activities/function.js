console.log(randomint());
console.log(nope);

function randomint(){
    console.log("Deterministic Message");
    return 4; // chosen by fair dice roll
}

var nope = function(){
    console.log("Why bother doing anything, when this won't work?");
    return 23;
}
