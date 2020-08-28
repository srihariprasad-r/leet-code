class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        
        for i in range(len(numbers)-1):  
            
            if i > 0 and numbers[i] == numbers[i-1]: continue
                
            left = i + 1                
            right = len(numbers) - 1
            
            while left <= right:
                csum = numbers[i] + numbers[left]
                if csum == target:
                    res.append([i+1,left+1])
                    left += 1                    
                    right -= 1
                elif csum < target:
                    left += 1
                else:     
                    right -= 1
                
        
        return res[0] if len(res) > 0 else res