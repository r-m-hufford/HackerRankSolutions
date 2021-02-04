/*
A teacher rounds students grades to the next divisible 
of 5 if they are within 2 points. Grades 37 and below 
are not rounded.
*/

grades = [73, 67, 38, 33]

function gradingStudents(grades) {
    const finalGrades = []
    for (let i = 0; i < grades.length; i++) {
        if (grades[i] <= 37) {
            finalGrades.push(grades[i])
        }
        else if ((grades[i] + 2) % 5 === 0) {
            finalGrades.push(Math.ceil(grades[i] / 5) * 5)
        }
        else if ((grades[i] + 1) % 5 === 0) {
            finalGrades.push(Math.ceil(grades[i] / 5) * 5)
        }
        else {
            finalGrades.push(grades[i])
        }
    }
    return (finalGrades)
}

console.log(gradingStudents(grades))