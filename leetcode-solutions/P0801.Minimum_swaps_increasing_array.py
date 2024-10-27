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


# DP - memo
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # need to add -1 to front of 2 lists
        nums1.insert(0, -1)
        nums2.insert(0, -1)

        def dfs(idx, dp, swapped):
            if idx == len(nums1):
                return 0

            if dp[idx][swapped] != -1:
                return dp[idx][swapped]
            res = float('inf')

            prev1 = nums1[idx-1]
            prev2 = nums2[idx-1]

            if swapped:
                prev1, prev2 = prev2, prev1

            if nums1[idx] > prev1 and nums2[idx] > prev2:
                res = dfs(idx+1, dp, 0)

            if nums1[idx] > prev2 and nums2[idx] > prev1:
                res = min(res, 1 + dfs(idx+1, dp, 1))

            dp[idx][swapped] = res
            return dp[idx][swapped]

        dp = [[-1 for _ in range(2)] for _ in range(len(nums1))]
        return dfs(1, dp, 0)

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        swp = [float('inf')] * len(nums1)
        no_swp = [float('inf')] * len(nums1)

        swp[0] = 1
        no_swp[0] = 0

        for i in range(1, len(nums1)):
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                swp[i] = swp[i-1] + 1
                no_swp[i] = no_swp[i-1]
            
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                swp[i] = min(swp[i], no_swp[i-1]+1)
                no_swp[i] = min(no_swp[i], swp[i-1])
        
        return min(swp[-1], no_swp[-1])        