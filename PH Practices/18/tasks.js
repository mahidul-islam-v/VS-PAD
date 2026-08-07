const calculateBill = (amount, taxRate = 0.05) => amount+amount*taxRate

const buildProfileCard = user => `${user.name}\n${user.title} at ${user.company}`

const getLowestPrice = prices => Math.min(prices)

console.log(getLowestPrice([340, 120, 560, 90]));

console.log(Math.min([1,2,3,4]))