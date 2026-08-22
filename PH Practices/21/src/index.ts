// Problem 01
function getBatteryStatus(percentage: number): string {
    let result: string

    if (percentage >= 0 && percentage <= 20) {
        result = "Low";
    } else if (percentage >= 21 && percentage <= 50) {
        result = "Medium";
    } else if (percentage >= 51 && percentage <= 90) {
        result = "High";
    } else if (percentage >= 91 && percentage <= 100) {
        result = "Full";
    } else {
        result = "Invalid Input";
    }

    return result;
}
console.log(getBatteryStatus(50));

// Problem 02
interface Booking {
    name: string;
    guests: number;
    time: string;
}

function formatBookingConfirmation(booking: Booking): string {
    return "aa"
}


console.log(getBatteryStatus(50));
