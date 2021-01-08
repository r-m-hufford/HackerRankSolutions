# BIRTHDAY CAKE CANDLES #
# return the the largest int in the list and count

candles = [4, 4, 1, 2]


def birthday_cake_candles(candles):
    return(candles.count(max(candles)))


print(birthday_cake_candles(candles))
