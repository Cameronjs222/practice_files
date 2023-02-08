// To find if a interger is a palindrom i must convert to a string, seperate into individual values, reverse the array, and join them back together.
function palendrome(x){
    return x.toString() === x.toString().split('').reverse().join('');

}

palendrome(25)
console.log(palendrome(25))