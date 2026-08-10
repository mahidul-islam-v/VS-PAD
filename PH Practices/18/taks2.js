const getFormattedPrices = prices => prices.map(price => `$${price}`)

const getAvailableProducts = products => products.filter(product => product.stock > 0)

const findProductByName = (products, name) => products.find(product => product.name == name)

const getTotalStockValue = products => products.reduce((accumulator, cur) => accumulator + cur.price * cur.stock, 0)

const getDiscountedTotalForCategory = (products, category) => products.filter(product => product.category == category).map(product => product.price * 0.9).reduce((accumulator, cur) => accumulator + cur, 0)

const sortByPriceAscending = products => products.sort((a,b)=> a.price - b.price) 

const applyBonusPoints = (users, bonus) => users.map(user =>{
    return { ...user, points: user.points + bonus }
})

const getTopSellingProduct = orders => {
    obj = orders.reduce((accumulator, cur) => accumulator ? accumulator.unitsSold > cur.unitsSold : cur, undefined)
    return obj.product
}


console.log(
    getTopSellingProduct([
        { product: "Pen", unitsSold: 30 },
        { product: "Bag", unitsSold: 12 },
        { product: "Pen", unitsSold: 25 },
    ]),
);