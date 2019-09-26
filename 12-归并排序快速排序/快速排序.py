import random

# 空间复杂度O(1) 原地排序
def quick_sort(nums):
    _quick_sort_between(nums, 0, len(nums) - 1)


def _quick_sort_between(nums, low, high):
    if low < high:
        # k = random.randint(low, high)
        # nums[low], nums[k] = nums[k], nums[low]

        m = _partition(nums, low, high)
        _quick_sort_between(nums, low, m - 1)
        _quick_sort_between(nums, m + 1, high)


def _partition(nums, low, high):
    pivot, j = nums[low], low
    for i in range(low + 1, high + 1):
        if nums[i] <= pivot:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[low], nums[j] = nums[j], nums[low]
    return j


test_ls = [3, 5, 38, 2, 1]
quick_sort(test_ls)
print(test_ls)
test_ls = [3]
quick_sort(test_ls)
print(test_ls)
test_ls = [3, 4]
quick_sort(test_ls)
print(test_ls)
test_ls = [5, 2, 3, 1]
quick_sort(test_ls)
print(test_ls)
