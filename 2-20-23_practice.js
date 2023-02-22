var romanToInt = function(s) {
    var value = 0;
    var string = s.split("").reverse()
    for (i=0;i<string.length;i++){ 
        if (string[i] == "I"){
            value += 1
        }
        if (string[i] == "V" && string[i+1] == "i"){
            i++
            value += 4
        }
        else if (string[i] == "V"){
            value += 5
        }
        if (string[i] == "X" && string[i+1] == "I"){
            i++
            value += 9
        }
        else if (string[i] == "X"){
            value += 10
        }
        if (string[i] == "L" && string[i+1] == "X"){
            i++
            value += 40
        }
        else if (string[i] == "L"){
            value += 50
        }
        if (string[i] == "C" && string[i+1] == "X"){
            i++
            value += 90
        }
        else if (string[i] == "C"){
            value += 100
        }
        if (string[i] == "D" && string[i+1] == "C"){
            i++
            value += 400
        }
        else if (string[i] == "D"){
            value += 500
        }
        if (string[i] == "M" && string[i+1] == "C"){
            i++
            value += 900
        }
        else if (string[i] == "M"){
            value += 1000
        }
    }
    console.log(value)
    console.log(string)
};
romanToInt("VIII")