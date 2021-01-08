# BIRTHDAY CAKE CANDLES #
# return the the largest int in the list and count

candles = [4, 4, 1, 2]


def birthday_cake_candles(candles):
    tallest_candle = 0
    for candle in candles:
        if candle > tallest_candle:
            tallest_candle = candle

    return(tallest_candle, candles.count(tallest_candle))


print(birthday_cake_candles(candles))
