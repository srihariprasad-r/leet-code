class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        lst = []

        cnt = 0

        def ok(arr, low, target):
            high = len(arr) - 1
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return False

        for i in range(len(nums)):
            if i > 0 and nums[i] - nums[i-1] == 0:
                continue

            if ok(nums, i + 1, nums[i] + k):
                cnt += 1

        return cnt