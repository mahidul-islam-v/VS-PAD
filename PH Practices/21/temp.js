"use strict";
const printUser = (name = "user", age = 0) => console.log(`${name} is ${age} years old.`);
const nayme = ["Me", 2020];
const mailTo = (obj) => obj.name + ' ' + (obj.mail ? obj.mail : "Not given");
console.log(mailTo({ name: "me", mail: "hah" }));
