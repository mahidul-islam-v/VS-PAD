"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function useState(inputValue) {
    function callMe(newInput) {
        return newInput;
    }
    return [inputValue, callMe(inputValue)];
}
console.log(useState("Yamete"));
//# sourceMappingURL=index.js.map