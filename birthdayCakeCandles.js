/* Birthday Candles
count how many items in
an array are the highest value */
candles = [1, 2, 3, , 3, 4]

function birthdayCakeCandles(candles) {
    high = 0
    highCount = 0

    for (let i = 0; i < candles.length; i++) {
        if (candles[i] > high) {
            high = candles[i]
        }
    }
    for (let i = 0; i < candles.length; i++) {
        if (candles[i] === high) {
            highCount += 1
        }
    }
    return (highCount)
}

console.log(birthdayCakeCandles(candles))