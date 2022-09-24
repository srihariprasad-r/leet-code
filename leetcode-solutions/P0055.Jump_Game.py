class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tgt = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= tgt:
                tgt = i

        return True if tgt == 0 else False


# TLE 
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums, idx, nb):
            if idx == len(nums)-1:
                return True

            next = idx + nums[idx]

            for i in range(idx+1, next+1):
                # if (i < len(nums) - 1 and nums[i] == 0):
                #     return False
                nb.add(i)
                if i < len(nums):
                    if dfs(nums, i, nb):
                        return True
                nb.remove(i)

            return False

        return dfs(nums, 0, set())
