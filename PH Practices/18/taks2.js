const getFormattedPrices = prices => prices.map(price => `$${price}`)

const getAvailableProducts = products => products.filter(product => product.stock > 0)

const findProductByName = (products, name) => products.find(product => product.name == name)

const getTotalStockValue = products => products.reduce((accumulator, cur) => accumulator + cur.price * cur.stock, 0)

const getDiscountedTotalForCategory = (products, category) => {
    
}
console.log(getTotalStockValue([{ price: 50, stock: 4 },{ price: 20, stock: 10 },]),);