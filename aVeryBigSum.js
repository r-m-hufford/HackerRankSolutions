// A VERY BIG SUM;

const numCopy = [1000, 194953, 24359808, 4329, 098];

function aVeryBigSum(ar) {
    return (ar.reduce(
        (accumulator, currentValue) => accumulator + currentValue)
    )
};

aVeryBigSum(numCopy)