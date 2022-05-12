class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        map = {}
        nums = list([int(c) for c in str(num)])
        for i, n in enumerate(nums):
            map[n] = i

        for idx, n in enumerate(nums):
            for d in range(9, n, -1):
                if d in map and map[d] > idx:
                    nums[idx], nums[map[d]] = nums[map[d]], nums[idx]
                    return int(''.join([str(c) for c in nums]))

        return num
