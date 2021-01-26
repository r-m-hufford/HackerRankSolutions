# FIND THE NUMBER #

# Given an unsorted array of n elements,
# find if the element k is present in the array or not.
# The function must return a string ‘YES’ or ‘NO’
# denoting if the element is present in the array or not.

list_of_numbers = [5, 3, 8, 7, 6, 1, 3, 2, 8]

k = 9


def in_list(arr, k):
    if k in arr:
        return 'YES'
    if not k in arr:
        return 'NO'


print(in_list(list_of_numbers, k))
