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
        def dfs(idx):
            if idx <= 0:
                return 0
            
            take = float('inf')
            no_take = float('inf')
            
            if nums1[idx] <= nums1[idx-1] or nums2[idx] <= nums2[idx-1]:
                nums1[idx-1], nums2[idx] = nums2[idx], nums1[idx-1]
                take = 1 + dfs(idx-1)
            else:
                no_take = dfs(idx-1)
            
            return min(take, no_take)
        
        return dfs(len(nums1)-1)