# simple_array_sum

ar = [562, 9348, 83, 1, 0, 12347]


def simpleArraySum(ar):
    simple_sum = 0
    for item in ar:
        simple_sum += item
    return simple_sum


print(simpleArraySum(ar))

# solution 2 #


def simple_array_sum(ar):
    return sum(ar)


print(simple_array_sum(ar))
