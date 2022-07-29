def squareroot(n):
    left = 1
    right = n

    while left < right:
        mid = left + (right-left) // 2

        if mid ** 2 >= n:
            right = mid
        else:
            left = mid + 1

    return right - 1


n = 81
print(squareroot(n))