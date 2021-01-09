//DIAGONAL DIFFERENCE;

/*      [1,2,3]
        [4,5,6]
        [9,8,9]
*/

let n = 3;
let arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]];


function diagonalDifference(arr) {
        sumOne = 0
        sumTwo = 0
        for (let i = 0; i < arr.length; i++) {
                sumOne += (arr[i][i])
        }
        for (let j = 0; j < arr.length; j++) {
                sumTwo += (arr[j][(arr.length - 1) - j])
        }
        return Math.abs(sumOne - sumTwo)
}

console.log(diagonalDifference(arr))
