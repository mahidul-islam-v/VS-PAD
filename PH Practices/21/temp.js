"use strict";
const printUser = (name = "user", age = 0) => console.log(`${name} is ${age} years old.`);
const nayme = ["Me", 2020];
const mailTo = (obj) => obj.name + ' ' + (obj.mail ? obj.mail : "Not given");
const chckr = (numba) => numba % 2 == 0 ? "even" : "odd";
const summr = (...numba) => numba.reduce((acc, curr) => acc + curr, 0);
const mrgr = (...numbers) => [...numbers];
console.log(mrgr(1, 2, 3, 411, 22, 33, 44));
