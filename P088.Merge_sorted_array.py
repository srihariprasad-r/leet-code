class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        pt1 = m - 1
        pt2 = n - 1
        
        for i in range(m+n-1, -1, -1):            
            if pt2 < 0 : break
                
            if pt1 >= 0 and nums1[pt1] > nums2[pt2]:
                nums1[i] = nums1[pt1]
                pt1 -= 1                   
            else:
                nums1[i] = nums2[pt2]
                pt2 -= 1
        
        return nums1