class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for _ in range(len(nums)):
            el = nums.pop(0)
            sublists = self.permute(nums)

            for sublist in sublists:
                sublist.append(el)

            res.extend(sublists)
            nums.append(el)

        return res
