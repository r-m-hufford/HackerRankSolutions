# ODDS #

# Given two integers, l and r, return all the odd
# numbers between l and r (l and r inclusive).
# The function must return an array of numbers.

def find_the_odds(l, r):
    odds = list(filter(lambda x: x % 2 != 0, range(l, r)))
    return odds


print(find_the_odds(3, 14))
