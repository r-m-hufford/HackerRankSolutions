# compare_triplets
peter = [1, 2, 3]
paul = [3, 2, 1]


def compare_triplets(a, b):
    final_score = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            final_score[0] += 1
        elif a[i] < b[i]:
            final_score[1] += 1
    return final_score


print(compare_triplets(peter, paul))
