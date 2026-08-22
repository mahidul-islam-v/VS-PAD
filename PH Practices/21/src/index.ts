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

type PaymentMethod = "cash" | "card" | "mobile";
interface Order {
    id: number;
    pay: PaymentMethod;
}

const o1: Order = {
    id: 1,
    pay: "card"
}



function getLastElement<T> (arr: T[]): T|undefined {
    return arr.at(-1);
}



interface Container<T> {
    item: T;
}

const c1: Container<string> = {
    item: "Book"
};
const c2: Container<number> = {
    item: 222
};