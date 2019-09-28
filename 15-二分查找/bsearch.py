def bsearch(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


test_nums, tar = [1, 2, 3, 4, 5], 4
print(bsearch(test_nums, tar))
