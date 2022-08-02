class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import deque
        
        arr = nums[:1]
        dec = deque(arr)
        for i, el in enumerate(nums[1:], 1):
            if i > k and dec[0] == arr[i-k-1]:
                dec.popleft()

            maxel = max(el, dec[0] + el)
            arr.append(maxel)
            while dec and dec[-1] < maxel:
                dec.pop()
            
            dec.append(maxel)
            
        return max(arr)