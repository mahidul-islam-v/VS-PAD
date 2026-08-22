"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function getBatteryStatus(percentage) {
    let result;
    if (percentage >= 0 && percentage <= 20) {
        result = "Low";
    }
    else if (percentage >= 21 && percentage <= 50) {
        result = "Medium";
    }
    else if (percentage >= 51 && percentage <= 90) {
        result = "High";
    }
    else if (percentage >= 91 && percentage <= 100) {
        result = "Full";
    }
    else {
        result = "Invalid Input";
    }
    return result;
}
console.log(getBatteryStatus(50));
//# sourceMappingURL=index.js.map