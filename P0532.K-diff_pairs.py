# submission has TLE

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        lst = []

        i = 0
        j = 1
        cnt = 0

        while i < len(nums) and j < len(nums):
            if k > 0 and nums[i] == nums[j]:
                while nums[i] == nums[j]:
                    j += 1
                    if j > len(nums) - 1:
                        i += 1
                        j = i + 1
            elif k == 0 and nums[i] == nums[j]:
                if (nums[i], nums[j]) not in lst:
                    lst.append((nums[i], nums[j]))
                    cnt += 1
                i += 1
                j += 1
            elif (nums[j] - nums[i] > k) or (nums[j] - nums[i] < k):
                j += 1
                if j > len(nums) - 1:
                    i += 1
                    j = i + 1
            else:
                if (nums[i], nums[j]) not in lst:
                    lst.append((nums[i], nums[j]))
                    cnt += 1
                i += 1
                j = i + 1

        return cnt