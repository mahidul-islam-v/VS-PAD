let val: unknown = "Hello TypeScript";

let numba: string | number = "100"

const number = typeof (numba) === "number" ? numba : Number(numba)

interface Product {
    title: string;
    price: number;
    inStock?: boolean;
}

const p1: Product = {
    title: "one",
    price: 9.99,
    inStock: true,
}
const p2: Product = {
    title: "Two",
    price: 0.99
};

function printPrice(product:Product):void {
    console.log(product.price)
}

printPrice(p1);
printPrice(p2);
