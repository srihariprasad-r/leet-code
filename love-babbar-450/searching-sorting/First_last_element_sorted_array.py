from bisect import bisect_left, bisect_right


def firstLast(arr, target):
    # base case
    if len(arr) == 0:
        return [-1, -1]

    left_idx = bisect_left(arr, target)
    right_idx = bisect_right(arr, target)

    if left_idx >= len(arr):
        left_idx = - 1

    if right_idx >= len(arr):
        right_idx = -1

    # need for test case: x not in arr
    return [left_idx if arr[left_idx] == target else -1, right_idx - 1 if right_idx > left_idx else -1]


def f_bisect_left(arr, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right-left) // 2
        if nums[mid] < target:  # < condition based on notes below
            left = mid + 1
        else:
            right = mid

    return left


def f_bisect_right(arr, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right-left) // 2
        if nums[mid] <= target:  # <= condition based on notes below
            left = mid + 1
        else:
            right = mid

    return right


nums = [5, 7, 7, 8, 8, 10]
target = 8
# print(firstLast(nums, target))
print(f_bisect_left(nums, target))
print(f_bisect_right(nums, target))
"""
# bisect_left :
  - for elements till arr[:i], e < x
  - for elements from arr[i:], e >= x
  
# bisect_right :
  - for elements till arr[:i], e <= x
  - for elements from arr[i:], e > x

 """
