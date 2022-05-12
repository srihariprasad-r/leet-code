#  Wrong submission

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = [0] * (len(nums)+1)
        map = {0:1}
        sum = cnt = 0
        
        for idx, num in enumerate(nums):
            sum += num
            prefix[idx+1] = sum

        for idx in range(1, len(prefix)):
            if prefix[idx] - k in map:
                map[prefix[idx]] += 1
                cnt += map[prefix[idx]]
            else:
                map[prefix[idx]] += 1

        return cnt
                