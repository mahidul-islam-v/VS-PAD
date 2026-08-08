const calculateBill = (amount, taxRate = 0.05) => amount+amount*taxRate

const buildProfileCard = user => `${user.name}\n${user.title} at ${user.company}`

const getLowestPrice = prices => Math.min(...prices)

const swapValues = (a, b) => [b, a]

const getEmployeeDept = employee => {
    return { title: employee.job.title, department: employee.job.department }
}
    
const promoteEmployee = (employee, newTitle) => {
    return {
        name: employee.name,
        title: newTitle,
    };
}

const sumAllPrices = prices => {
    let x = 0
    for (price of prices) {
        x += price
    }
    return x
}

const getManagerName = employee => employee?.manager?.name

const splitFirstRest = arr => { first: arr[0];  rest: arr.slice(1)} 

console.log(splitFirstRest([10, 20, 30, 40]));
