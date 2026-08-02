function matchWinner(teamAGoals, teamBGoals) {

    if (typeof teamAGoals !== "number" || typeof teamBGoals !== "number") {
        return "Invalid";
    }

    if (teamAGoals > teamBGoals){
        return "Team A Won";
    } else if (teamBGoals > teamAGoals) {
        return "Team B Won";
    } else{
        return "Draw";
    }
}

function isElevatorSafe(weights) {

    if (!Array.isArray(weights)) {
        return "Invalid";
    }

    let totalWeight = 0;
    for (let i = 0; i < weights.length; i++) {
        totalWeight += weights[i];
    }

    if (totalWeight <= 400) {
        return true;
    } else {
        return false;
    }
}

function calculateAiCost(tokensUsed) {
    if (typeof tokensUsed !== "number" || tokensUsed < 0) {
        return "Invalid";
    }

    if (tokensUsed <= 500) {
        return 0;
    } else {
        return Math.ceil((tokensUsed-500)/100)*5
    }

    // !! There is a logic error in the sample test cases. We either have to consider charge after each 100 token used or consider the cost when the first token is used fro mthe next 100 token. If 650 token chrages 5 taka, then 1000 token should have charged 20 taka not 25. Or 650 token should have been charged 10 taka if 100 token charges 25 taka.
    
    // ? I went with the more realistic method, the 2nd one, which is 5 taka charged when you use the 1st token of the next 100.
}

function topRatedRestaurant(restaurants) {
    if (!Array.isArray(restaurants) || restaurants.length == 0) {
        return "Invalid";
    }

    ratings = restaurants.values()

    Math.max(ratings)

    return ratings
}


console.log(
    topRatedRestaurant([
        { name: "Chillox", rating: 4.5 },
        { name: "Sultan's Dine", rating: 4.8 },
    ]),
);
