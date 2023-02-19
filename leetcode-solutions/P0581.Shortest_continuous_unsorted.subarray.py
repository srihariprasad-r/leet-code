# Method 1 - TLE

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = len(nums)
        right = 0

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    left = min(left, i)
                    right = max(right, j)

        return right - left + 1 if right - left + 1 > 0 else 0

# Method 2 


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = len(nums)
        right = 0

        t = sorted(nums, key=lambda x: x)

        for i in range(len(nums)):
            if t[i] != nums[i]:
                left = min(left, i)
                right = max(right, i)

        return right - left + 1 if right - left > 0 else 0
