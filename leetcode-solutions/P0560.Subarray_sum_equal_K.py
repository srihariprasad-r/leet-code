class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = [nums[0]]
        map = defaultdict(int)
        map[0] = 1
        sum = cnt = 0

        for idx in range(1, len(nums)):
            sum = nums[idx] + prefix[idx-1]
            prefix.append(sum)

        for idx, num in enumerate(prefix):
            if num - k in map:
                cnt += map[num-k]

            map[num] += 1

        return cnt

# Method 2 - similar to above (wrong submission)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {}
        mp[0] = 1
        cnt = 0
        prefix = [0] * len(nums)

        for i in range(1,len(nums)):
            prefix[i] = nums[i] + prefix[i-1]

        for i in range(len(nums)):
            diff = abs(nums[i] - k)

            if diff in mp:
                cnt += mp[diff] 
                mp[diff] += 1
            mp[diff] = 1

        return cnt
