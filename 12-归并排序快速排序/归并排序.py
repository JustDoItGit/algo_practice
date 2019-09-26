def merge_sort(nums):
    n = len(nums)
    _merge_sort_between(nums, 0, n - 1)


def _merge_sort_between(nums, low, high):
    if low < high:
        mid = (low + high) // 2
        _merge_sort_between(nums, low, mid)
        _merge_sort_between(nums, mid + 1, high)
        _merge(nums, low, mid, high)


def _merge(nums, low, mid, high):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    if i <= mid:
        start = i
        end = mid
    else:
        start = j
        end = high
    tmp.extend(nums[start: end + 1])
    nums[low:high + 1] = tmp


test_ls = [3, 5, 38, 2, 1]
merge_sort(test_ls)
print(test_ls)
test_ls = [3]
merge_sort(test_ls)
print(test_ls)
test_ls = [3, 4]
merge_sort(test_ls)
print(test_ls)
test_ls = [5, 2, 3, 1]
merge_sort(test_ls)
print(test_ls)
