/* plusMinus 
ratio of zero, positive and negative values
to the total number of elemenets in an array
*/

const arr = [1, -1, 0, 1, -1, 1]

function plusMinus(arr) {
    let zero = []
    let gtrThanOne = []
    let lessThanOne = []

    for (let i = 0; i <= arr.length; i++) {
        if (arr[i] === 0) {
            zero.push(arr[i])
        } else if (arr[i] > 0) {
            gtrThanOne.push(arr[i])
        } else if (arr[i] < 0) {
            lessThanOne.push(arr[i])
        }
    }
    console.log(gtrThanOne.length / arr.length);
    console.log(lessThanOne.length / arr.length);
    console.log(zero.length / arr.length);
}

plusMinus(arr)