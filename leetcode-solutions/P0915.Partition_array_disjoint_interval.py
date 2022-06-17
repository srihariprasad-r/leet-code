class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftArray = [0] * len(nums)
        rightArray = [0] * len(nums)
        n = len(nums)

        i = 0
        j = n - 1

        lmax = float('-inf')
        while i < n:
            lmax = max(lmax, nums[i])
            leftArray[i] = lmax

            i += 1

        rmin = float('inf')
        while j >= 0:
            rmin = min(rmin, nums[j])
            rightArray[j] = rmin

            j -= 1

        for i in range(1, len(nums)):
            if leftArray[i-1] <= rightArray[i]:
                return i
