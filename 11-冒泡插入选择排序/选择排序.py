from typing import List


def selection_sort(a: List[int]):
    length = len(a)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if a[min_index] > a[j]:
                min_index = j
        if min_index != i:
            a[min_index], a[i] = a[i], a[min_index]


test_ls = [3, 5, 38, 2, 1]
selection_sort(test_ls)
print(test_ls)
test_ls = [3]
selection_sort(test_ls)
print(test_ls)
test_ls = [3, 4]
selection_sort(test_ls)
print(test_ls)
test_ls = [5, 2, 3, 1]
selection_sort(test_ls)
print(test_ls)
