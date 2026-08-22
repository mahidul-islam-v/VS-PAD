"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// Problem 01
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
function formatBookingConfirmation(booking) {
    return `${booking.name}'s table for ${booking.guests} guests is confirmed at ${booking.time}.`;
}
console.log(formatBookingConfirmation({ name: "Aisha", guests: 4, time: "7:00 PM" }));
//# sourceMappingURL=index.js.map