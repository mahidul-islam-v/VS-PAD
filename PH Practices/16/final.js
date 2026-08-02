function matchWinner(teamAGoals, teamBGoals) {
    if (teamAGoals > teamBGoals){
        return "Team A Won";
    } else if (teamBGoals > teamAGoals) {
        return "Team B Won";
    } else if (teamAGoals === teamBGoals) {
        return "Draw";
    } else {
        return "Invalid";
    }
}

function isElevatorSafe(weights) {
    let totalWeight = 0;
    for (let i = 0; i < weights.length; i++) {
        totalWeight += weights[i];
    }
    return totalWeight
    if (totalWeight <= 400) {
        return true;
    } else if (totalWeight > 400) {
        return false;
    } else {
        return "Invalid";
    }
}


console.log(isElevatorSafe([10,20,"30"]))

