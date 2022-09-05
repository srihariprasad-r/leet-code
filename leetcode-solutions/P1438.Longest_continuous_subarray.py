class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        dec = deque()
        inc = deque()
        
        ans = 0
        left = 0
        
        for idx, el in enumerate(nums):
            while dec and el > dec[-1]:
                dec.pop()
                
            dec.append(el)
            
            while inc and el < inc[-1]:
                inc.pop()
                
            inc.append(el)
            
            while dec[0] - inc[0] > limit:
                if dec[0] == nums[left]:
                    dec.popleft()
                    
                if inc[0] == nums[left]:
                    inc.popleft()
                    
                left += 1
                    
            ans = max(ans, idx - left + 1)
                
        return ans