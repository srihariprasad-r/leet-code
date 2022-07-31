def foursum(arr, tgt):
    arr.sort()
    ans = set()

    for i in range(len(arr)-3):
        for j in range(i+1, len(arr)-2):
            left = j + 1
            right = len(arr) - 1
            while left < right:
                if arr[i] + arr[j] + arr[left] + arr[right] == tgt:
                    ans.add((arr[i], arr[j], arr[left], arr[right]))

                if arr[i] + arr[j] + arr[left] + arr[right] > tgt:
                    right -= 1
                else:
                    left += 1

    return ans


arr = [10, 2, 3, 4, 5, 7, 8]
print(foursum(arr, 23))