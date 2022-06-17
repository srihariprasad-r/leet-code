class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()

        ans = set()

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        left += 1

        return list(ans)