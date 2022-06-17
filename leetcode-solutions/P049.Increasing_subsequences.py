class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()

        def backtrack(idx, cur):
            if len(cur) > 1:
                ans.add(tuple(cur))

            lst = cur[-1] if cur else -999

            for i in range(idx, len(nums)):
                if lst <= nums[i]:
                    cur.append(nums[i])
                    backtrack(i+1, cur)
                    cur.pop()

            return ans

        return sorted(backtrack(0, []))
