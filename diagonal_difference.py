n = 3
arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]


def diagonalDifference(arr):
    sum_one = 0
    sum_two = 0
    for i in range(n):
        sum_one += (arr[i][i])
    for j in range(n):
        sum_two += (arr[j][(n-1) - j])
    return(abs(sum_one - sum_two))


print(diagonalDifference(arr))
