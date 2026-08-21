"use strict";
function useState(inputValue) {
    function callMe(newInput) {
        return newInput;
    }
    return [inputValue, callMe(inputValue)];
}
console.log(useState("Yamete"));
