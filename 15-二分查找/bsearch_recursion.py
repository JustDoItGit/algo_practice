def bsearch(nums, target):
    return bsearch_internally(nums, 0, len(nums) - 1, target)


def bsearch_internally(nums, low, high, target):
    if low > high:
        return -1

    mid = low + (high - low >> 1)
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return bsearch_internally(nums, mid + 1, high, target)
    else:
        return bsearch_internally(nums, low, mid - 1, target)


test_nums, tar = [1, 2, 3, 4, 5], 4
print(bsearch(test_nums, tar) == 3)
