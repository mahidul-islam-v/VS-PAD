const getFormattedPrices = prices => prices.map(price => `$${price}`)

const getAvailableProducts = products => products.filter(product => product.stock > 0)

const findProductByName = (products, name) => products.find(product => product.name == name)

console.log(
    findProductByName(
        (products = [
            { name: "Pen", price: 10 },
            { name: "Bag", price: 500 },
        ]),
        (name = "Bag"),
    ),
);