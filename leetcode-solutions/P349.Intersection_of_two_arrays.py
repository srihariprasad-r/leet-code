class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from sets import Set
        
        l1 = Set(nums1)
        l2 = Set(nums2)
        
        
        return [x for x in l1.intersection(l2)]