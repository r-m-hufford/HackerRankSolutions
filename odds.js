/* 
given a range which begins at l and terminates 
at r return all odd numbers within the range
*/

function oddNumbers(l, r) {
    let arr = []
    for (i = l; i >= l && i <= r; i++) {
        if (i % 2 !== 0) {
            arr.push(i)
        };
    };
    return arr
};

console.log(oddNumbers(3, 14))