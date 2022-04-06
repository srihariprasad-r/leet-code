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
