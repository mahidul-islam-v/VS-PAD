const calculateBill = (amount, taxRate = 0.05) => amount+amount*taxRate

const buildProfileCard = user => `${user.name}\n${user.title} at ${user.company}`

const getLowestPrice = prices => Math.min(...prices)

const swapValues = (a, b) => [b, a]

console.log(swapValues(5, 10));
