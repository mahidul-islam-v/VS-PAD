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

    let cost = 5;

    if (tokensUsed <= 500) {
        return 0;
    } else {
        return (tokensUsed-500)
    }
}


console.log(matchWinner(2,2))
