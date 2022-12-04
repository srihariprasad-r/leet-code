# Wrong submission

class Solution(object):
    def minSwap(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def backtrack(idx, ln, swaps, ans=float('inf')):
            if idx == ln:
                ans = min(ans, swaps)
                return ans

            if nums1[idx] > nums1[idx-1] and nums2[idx] > nums2[idx-1]:
                ans = min(ans, backtrack(idx+1, ln, swaps, ans))

            if nums1[idx] > nums2[idx-1] and nums2[idx] > nums1[idx-1]:
                nums1[idx], nums2[idx] = nums2[idx], nums1[idx]
                ans = min(ans, backtrack(idx+1, ln, swaps+1, ans))
                nums1[idx], nums2[idx] = nums2[idx], nums1[idx]

            return ans

        n = len(nums1)
        return backtrack(1, n, 0)


# wrong submission

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        def dfs(idx, dp, ans=0):
            if idx >= len(nums1):
                return ans

            if dp[idx] > -1:
                return dp[idx]

            take = float('inf')
            no_take = float('inf')

            if nums1[idx] > nums1[idx-1] and nums2[idx] > nums2[idx-1]:
                no_take = dfs(idx+1, dp, ans)

            if nums1[idx] > nums2[idx-1] and nums2[idx] > nums1[idx-1]:
                nums1[idx], nums2[idx] = nums2[idx], nums1[idx]
                take = dfs(idx+1, dp, ans + 1)
                nums1[idx], nums2[idx] = nums2[idx], nums1[idx]

            dp[idx] = min(take, no_take)

            return dp[idx]

        dp = [-1 for _ in range(len(nums1))]
        dfs(1, dp)
        return dp[-1]
