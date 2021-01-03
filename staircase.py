# STAIRCASE #
num = 6


def staircase(x):
    for i in range(x):
        print(" " * (x - i), "*" * i)


staircase(num)
