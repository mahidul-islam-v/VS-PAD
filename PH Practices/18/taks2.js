const getFormattedPrices = prices => prices.map(price => `$${price}`)

const getAvailableProducts = products => products.filter(product => product.stock > 0)

const findProductByName = (products, name) => products.find(product => product.name == name)

const getTotalStockValue = products => products.reduce((accumulator, cur) => accumulator + cur.price * cur.stock, 0)

const getDiscountedTotalForCategory = (products, category) => {
    obj = products.find(product => product.category == category)
    
}
console.log(
    getDiscountedTotalForCategory(
        (products = [
            { name: "Pen", category: "stationery", price: 100 },
            { name: "Bag", category: "accessory", price: 500 },
            { name: "Notebook", category: "stationery", price: 60 },
        ]),
        (category = "stationery"),
    ),
);