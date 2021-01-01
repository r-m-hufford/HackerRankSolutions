# PLUS MINUS #
arr = [1, 2, 0, -1, -1]


def plus_minus(arr):
    positive = 0
    negative = 0
    zero = 0

    for number in arr:
        if number > 0:
            positive += 1
        if number < 0:
            negative += 1
        if number == 0:
            zero += 1

    print(positive/len(arr),
          '\n', negative/len(arr),
          '\n', zero/len(arr))
