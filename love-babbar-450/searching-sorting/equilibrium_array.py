def equilibriumArray(arr):
    ls = [arr[0]]
    rs = [arr[-1]] * len(arr)

    # left sum prefix
    for i in range(1, len(arr)):
        ls.append(ls[-1] + arr[i])

    # right sum prefix
    for i in range(len(arr)-2, 0, -1):
        rs[i] = rs[i+1] + arr[i]

    for i in range(len(arr)):
        if ls[i] == rs[i]:
            return i


arr = [1, 2, 6, 4, 0, -1]
print(equilibriumArray(arr))
