class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        stck = []
        ans = []
        
        for n in nums2:
            while stck and stck[-1] < n:
                map[stck[-1]] = n
                stck.pop()
                
            stck.append(n)
            
        for k in nums1:
            if not(k in map):
                ans.append(-1)
            else:
                ans.append(map[k])
                
        return ans