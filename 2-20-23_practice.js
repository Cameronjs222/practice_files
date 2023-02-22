var romanToInt = function(s) {
    var value = 0;
    var string = s.split("") //need to figure out how to define iv as 4
    for (i=0;i<string.length;i++){ 
        if (string[i] == "i" || string[i] == "I"){
            value += 1
        }
    }
    console.log(value)
};