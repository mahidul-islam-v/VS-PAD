function studentIntroduction(student) {
    if (typeof (student) != "object" || student.name == undefined || student.age == undefined || student.course == undefined) {
        return "Invalid"
    } else {
        return `My name is ${student.name}. I am ${student.age} years old. I am learning ${student.course}`
    }
}

function filterActiveUsers(users) {
    if (!Array.isArray(users) || users.length == 0 || users.filter((user) => user.isActive==undefined).length != 0) {
        return "Invalid"
    } else {
        return users.filter(user => user.isActive == true)
    }
}

function countHashtags(caption) {
    words = [...caption.split(" ")]
    tags = words.filter(word => word[0] == "#")
    longest = tags.reduce(
        (longest, cur) => (longest.length > cur.length ? longest : cur),
        "",
    );

    return {
        hashtagCount: tags.length,
        longestTag: longest
    };
}


console.log(countHashtags("Loving this weather today #sunny #vibes #weekend"));