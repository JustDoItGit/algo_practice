from typing import List


def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(1, length):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break


test_ls = [3, 5, 38, 2, 1]
insertion_sort(test_ls)
print(test_ls)
test_ls = [3]
insertion_sort(test_ls)
print(test_ls)
test_ls = [3, 4]
insertion_sort(test_ls)
print(test_ls)
test_ls = [5, 2, 3, 1]
insertion_sort(test_ls)
print(test_ls)
