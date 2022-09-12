class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mp = {}
        for n in nums:
            if not(n in mp):
                mp[n] = 1
            else:
                mp[n] += 1

        ans = [v for v in mp.values() if v >= 2]

        return True if ans else False
