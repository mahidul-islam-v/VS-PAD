let val: unknown = "Hello TypeScript";

let numba: string | number = "100"

const number = typeof(numba) === "number" ? numba : Number(numba)

console.log(number+10);
