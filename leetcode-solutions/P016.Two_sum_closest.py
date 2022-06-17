class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        nums.sort()

        mingap = float('inf')
        ans = 0

        for i in range(len(nums)-2):
            low = i + 1
            high = len(nums)-1
            while low != high:
                sum_el = nums[i] + nums[low] + nums[high]

                if sum_el == target:
                    return target
                elif sum_el < target:
                    low += 1
                else:
                    high -= 1

                if abs(sum_el - target) < mingap:
                    mingap = abs(sum_el - target)
                    ans = sum_el

        return ans