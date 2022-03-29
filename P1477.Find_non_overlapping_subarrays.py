# wrong submission

class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        i, j, rsum = 0, 1, 0
        res = []

        while j < len(arr):
            if arr[i] == target:
                res.append([arr[i]])

            rsum += arr[j]

            if rsum == target:
                res.append([arr[i], arr[j]])

            while rsum > target:
                rsum -= arr[i]
                i += 1

            j += 1

        arr = sorted(res, key=lambda x: len(x))

        return -1 if len(res) < 2 else 2
