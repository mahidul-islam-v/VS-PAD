function studentIntroduction(student) {
    if (typeof (student) != "object" || student.name == undefined || student.age == undefined || student.course == undefined) {
        return "Invalid"
    } else {
        return `My name is ${student.name}. I am ${student.age} years old. I am learning ${student.course}`
    }
}

function filterActiveUsers(users) {
    // Write your code here
}


console.log(studentIntroduction("student"));