function matchWinner(teamAGoals, teamBGoals) {
    if (teamAGoals > teamBGoals){
        return "Team A Won"
    } else if (teamBGoals > teamAGoals) {
        return "Team A Won"
    } else {
        return "Draw"
    }
}

