const getFormattedPrices = prices => prices.map(price => `$${price}`)

const getAvailableProducts = products => products.filter(product => product.stock > 0)

const findProductByName = (products, name) => products.find(product => product.name == name)

const getTotalStockValue = products => products.reduce((accumulator, cur) => accumulator + cur.price * cur.stock, 0)

const getDiscountedTotalForCategory = (products, category) => products.filter(product => product.category == category).map(product => product.price * 0.9).reduce((accumulator, cur) => accumulator + cur, 0)

const sortByPriceAscending = products => {
    return products.sort((a,b)=> a.price - b.price) 
}



console.log(
    sortByPriceAscending([
        { name: "Bag", price: 500 },
        { name: "Pen", price: 10 },
        { name: "Notebook", price: 60 },
    ]),
);