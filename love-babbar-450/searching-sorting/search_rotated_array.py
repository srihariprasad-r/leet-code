def rotated_array(arr, target):
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= target and target < arr[mid]:
                right = mid
            else:
                left = mid + 1
        else:
            if arr[right] >= target and target > arr[mid]:
                left = mid + 1
            else:
                right = mid

    return left if arr[left] == target else -1


arr = [4, 5, 6, 7, 0, 1, 2]
target = 4
print(rotated_array(arr, target))
