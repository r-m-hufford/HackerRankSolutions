/* MINI MAX */

ar = [2, 5, 4, 3, 1, 6]

function miniMax(ar) {
    let max = Math.max(...ar)
    let min = Math.min(...ar)
    let sum = ar.reduce((acc, cur) => acc + cur)
    console.log(sum - max, sum - min)
}

miniMax(ar)