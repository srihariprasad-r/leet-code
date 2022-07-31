def pairWithdifference(arr, N):
    def binarysearch(arr, tgt):
        left = 0
        right = len(arr) - 1

        mid = left + (right - left) // 2

        if arr[mid] == tgt:
            return mid

        if arr[mid] > tgt:
            right = mid - 1
        else:
            left = mid

        return - 1

    for i in range(len(arr)):
        pair_element = arr[i] - N

        idx = binarysearch(arr, pair_element)
        if idx == -1:
            continue
        else:
            return (arr[i], arr[idx])

    return -1


arr = [90, 70, 20, 80, 50]
N = 80
print(pairWithdifference(arr, N))