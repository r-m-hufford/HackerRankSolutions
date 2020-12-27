// COMPARE TRIPLETS;

let sid = [3, 3, 3];
let nancy = [3, 2, 1];

function compareTriplets(a, b) {
    let score = [0, 0]
    for (let i = 0; i < b.length; i++) {
        if (a[i] > b[i]) {
            score[0] += 1
        } else if (a[i] < b[i]) {
            score[1] += 1
        };
    };
    return score
};

console.log(compareTriplets(sid, nancy))