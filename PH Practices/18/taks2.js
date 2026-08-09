const getFormattedPrices = prices => prices.map(price => `$${price}`)

const getAvailableProducts = products => products.filter(product => product.stock > 0)
    
console.log(
    getAvailableProducts([
        { name: "Pen", stock: 5 },
        { name: "Bag", stock: 0 },
        { name: "Notebook", stock: 2 },
    ]),
);