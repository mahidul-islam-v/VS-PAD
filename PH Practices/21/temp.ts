const printUser = (name:string = "user", age:number = 0) => console.log(`${name} is ${age} years old.`);

const nayme: [string, number] = ["Me", 2020];


const mailTo = (obj: { name: string, mail?: string }): string => obj.name + ' ' + (obj.mail ? obj.mail : "Not given") 

const chckr = (numba:number):string => numba%2==0 ? "even" : "odd" 


console.log(mailTo({name: "me", mail: "hah"}))