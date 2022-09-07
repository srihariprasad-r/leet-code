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
