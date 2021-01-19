# given a range, and 2 points, determine if
# moving a given number of spaces from either
# point will land within the range.

# In the problem, the range is represented as a
# house and the 2 points are trees with fruit that
# falls off of them. The question is - will the
# fruit land on the house?

s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]


def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apple_dist = [app + a for app in apples]
    apples_in_range = [app for app in apple_dist if s <= app <= t]

    orange_dist = [org + b for org in oranges]
    oranges_in_range = [org for org in orange_dist if s <= org <= t]

    result = [len(apples_in_range), len(oranges_in_range)]

    print(*result, sep='\n')


count_apples_and_oranges(s, t, a, b, apples, oranges)
