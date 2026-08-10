function studentIntroduction(student) {
    if (typeof (student) != "object" || student.name == undefined || student.age == undefined || student.course == undefined) {
        return "Invalid"
    } else {
        return `My name is ${student.name}. I am ${student.age} years old. I am learning ${student.course}`
    }
}

function filterActiveUsers(users) {
    if (!Array.isArray(users) || users.length == 0 || users.find((user) => user.isActive==undefined)) {
        return "Invalid"
    } else {
        return users.filter(user => user.isActive == true)
    }
}

function countHashtags(caption) {
    if (typeof caption != "string") {
        return "Invalid";
    } else {
        words = [...caption.split(" ")];
        tags = words.filter(word => word.startsWith("#"));
        longest = tags.reduce(
            (longest, cur) => (longest.length >= cur.length ? longest : cur),
            "",
        );

        return {
            hashtagCount: tags.length,
            longestTag: longest.slice(1),
        };
    }
}


function bonusScore(scores) {
    if (!Array.isArray(scores) || scores.length == 0 || scores.find(score => typeof (score) != "number")) {
        return "Invalid"
    } else {
        return scores.map(score => score+10).reduce((total, cur) => total+cur, 0)
    }
    
}

function generateLeaderboard(students) {
    if (!Array.isArray(students)) {
        return "Invalid";
    }

    if (students.length == 0) {
        return "Invalid";
    }

    if (students.find(student => (student.name == undefined || student.score == undefined))) {
        return "Invalid";
    }

    if (students.find(student => typeof (student.score) != "number")) {
        return "Invalid"
    }

    const qualified = students.filter(student => {
        return student.score >= 70;
    });

    const names = qualified.map((student) => {
        return student.name.toUpperCase();
    });

    return names.slice(0, 3);
}




console.log(generateLeaderboard([{ name: "Rafi", score: "90" }]));
