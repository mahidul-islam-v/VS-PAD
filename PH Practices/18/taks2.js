const getFormattedPrices = prices => prices.map(price => `$${price}`)

const getAvailableProducts = products => products.filter(product => product.stock > 0)

const findProductByName = (products, name) => products.find(product => product.name == name)

const getTotalStockValue = products => products.reduce((accumulator, cur) => accumulator + cur.price * cur.stock, 0)

const getDiscountedTotalForCategory = (products, category) => products.filter(product => product.category == category).map(product => product.price * 0.9).reduce((accumulator, cur) => accumulator + cur, 0)

const sortByPriceAscending = products => products.sort((a,b)=> a.price - b.price) 

const applyBonusPoints = (users, bonus) => {
    arr = [...users]
    arr.map(user => {
        arr2 = user
        arr2.points += bonus

        return arr2
    }
    )
    return arr
}


console.log(
    applyBonusPoints((users = [{ name: "Rafi", points: 20 }]), (bonus = 5)),
);