"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
let val = "Hello TypeScript";
let numba = "100";
const number = typeof (numba) === "number" ? numba : Number(numba);
const p1 = {
    title: "one",
    price: 9.99,
    inStock: true,
};
const p2 = {
    title: "Two",
    price: 0.99
};
function printPrice(product) {
    console.log(product.price);
}
const o1 = {
    id: 1,
    pay: "card"
};
function getLastElement(arr) {
    return arr.at(-1);
}
console.log(getLastElement(["1", "a"]));
//# sourceMappingURL=index.js.map