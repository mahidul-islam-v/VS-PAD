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
}


console.log(isElevatorSafe([10,20,30]))

