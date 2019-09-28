def bsearch_left(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            if mid == 0 or nums[mid - 1] != target:
                return mid
            else:
                high = mid - 1
    return -1


def bsearch_right(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                return mid
            else:
                low = mid + 1
    return -1


def bsearch_left_not_less(nums, target):
    """查找第一个大于等于给定值的元素"""
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] >= target:
            if mid == 0 or nums[mid - 1] < target:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1


def bsearch_right_not_greater(nums, target):
    """查找最后一个小于等于给定值的元素"""
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid - 1
        else:
            if mid == len(nums) - 1 or nums[mid + 1] > target:
                return mid
            else:
                low = mid + 1
    return -1


if __name__ == "__main__":
    a = [1, 1, 2, 3, 4, 6, 7, 7, 7, 7, 10, 22]

    print(bsearch_left(a, 0) == -1)
    print(bsearch_left(a, 7) == 6)
    print(bsearch_left(a, 30) == -1)

    print(bsearch_right(a, 0) == -1)
    print(bsearch_right(a, 7) == 9)
    print(bsearch_right(a, 30) == -1)

    print(bsearch_left_not_less(a, 0) == 0)
    print(bsearch_left_not_less(a, 5) == 5)
    print(bsearch_left_not_less(a, 30) == -1)

    print(bsearch_right_not_greater(a, 0) == -1)
    print(bsearch_right_not_greater(a, 6) == 5)
    print(bsearch_right_not_greater(a, 30) == 11)
