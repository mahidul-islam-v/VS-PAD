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

// Problem 02
interface Booking {
    name: string;
    guests: number;
    time: string;
}
function formatBookingConfirmation(booking: Booking): string {
    return `${booking.name}'s table for ${booking.guests} guests is confirmed at ${booking.time}.`;
}

// Problem 03
function calculateWeeklyTotal(expenses: number[]): number {
    return expenses.reduce((acc:number, cur:number): number => acc+cur, 0)
}

// Problem 04
type Light = "red" | "yellow" | "green"
function getTrafficAction(light: Light): string {
    return light=="red" ? "Stop" : light == "yellow" ? "Slow Down" : "Go"
}

// Problem 05
interface Summary {
    total: number;
    average: number;
}
function getQuizSummary(scores: number[]): Summary  {
    let t: number = scores.reduce((acc: number, cur: number): number => acc + cur, 0)
    let a: number = scores.length == 0 ? 0 : (t/scores.length)
    return {
        total: t,
        average: a
    };
}