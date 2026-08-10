function studentIntroduction(student) {
    if (typeof (student) != "object" || student.name == undefined || student.age == undefined || student.course == undefined) {
        return "Invalid"
    } else {
        return `My name is ${student.name}. I am ${student.age} years old. I am learning ${student.course}`
    }
}

function filterActiveUsers(users) {
    if (typeof (users) != "array" || users.length == 0 || users.filter((user) => user.isActive==undefined).length != 0) {
        return 222111
    }
}


console.log(filterActiveUsers([{name:"A", isActive:true},{name:"B", isActive:false}]));