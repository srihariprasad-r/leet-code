class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.append(0)
        sum = 0
        stck = [-1]

        for idx, el in enumerate(arr):
            while stck and el < arr[stck[-1]]:
                idx1 = stck.pop()
                left = idx1 - stck[-1]
                right = idx - idx1
                sum += left * arr[idx1] * right
            stck.append(idx)

        return sum % (10**9+7)

# wrong submission
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        c = 0
        res = [[float('inf') for _ in range(len(arr))] for _ in range(len(arr))]

        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if i == j:
                    res[i][j] = arr[i]
                else:
                    res[i][j] = min(min(arr[i:j+1]), res[i][j])
                c += res[i][j]

        return c % (10**9+7)

# wrong submission
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        prev = [i+1 for i in range(len(arr))]
        nxt = [len(arr)-i for i in range(len(arr))]
        stck = []
        ans = 0

        for i in range(len(arr)):
            while stck and arr[stck[-1]] > arr[i]:
                x = stck.pop()
            if stck: prev[i] = i - stck[-1]
            stck.append(i)

        stck = []

        for i in range(len(arr)):
            while stck and arr[stck[-1]] > arr[i]:
                x = stck.pop()
                nxt[x] = i - x
            stck.append(i)

        for i in range(len(arr)):
            ans += (prev[i]*nxt[i]*arr[i]) % 100_000_007

        return ans