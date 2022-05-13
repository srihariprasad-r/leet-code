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
