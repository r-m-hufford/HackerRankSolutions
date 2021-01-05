# MINI MAX #
# sort the list, find sum from 0 to -2 and 1 to the end #

list_1 = [2, 4, 1, 5, 6, 3]


def mini_max_sum(arr):
    arr.sort()
    min_sum = sum(arr[:-1])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)


mini_max_sum(list_1)

# solution 2 #


def mini_max_two(arr):
    min_sum = sum(arr) - max(arr)
    max_sum = sum(arr) - min(arr)
    print(min_sum, max_sum)


mini_max_two(list_1)

# solution 3 #


def mini_max_three(arr):
    return (sum(arr) - max(arr), sum(arr) - min(arr))


print(*mini_max_three(list_1))
