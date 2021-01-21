// given a list of numbers, 
// determine if k is present


listOfNumbers = [1, 4, 7, 9, 8, 3, 2]

function findNum(arr, k) {
    if (arr.includes(k) === true) {
        return ('YES')
    } else {
        return ('NO')
    }
};

console.log(findNum(listOfNumbers, 9))