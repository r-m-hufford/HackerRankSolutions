/* SIMPLE ARRAY SUM */

listOfNumbers = [562, 9348, 83, 1, 0, 12347]

function simpleArraySum(ar) {
    let sum = ar.reduce((acc, val) => acc + val)
    return sum
}

console.log(simpleArraySum(listOfNumbers))