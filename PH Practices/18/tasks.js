const calculateBill = (amount, taxRate = 0.05) => amount+amount*taxRate

const buildProfileCard = user => `${user.name}\n${user.title} at ${user.company}`

const getLowestPrice = prices => Math.min(...prices)

const swapValues = (a, b) => [b, a]

const getEmployeeDept = employee => {
        return { title: employee.job.title, department: employee.job.department }
    }
    
console.log(getEmployeeDept({ name: "Nadia", job: { title: "PM", department: "Product" } }));
