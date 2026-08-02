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
    
}


console.log(matchWinner(2,"2"))

