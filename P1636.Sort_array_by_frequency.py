class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for i in range(len(nums)):
            if not(nums[i] in freq):
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        
        def sortfunc(n1, n2):
            freq1 = freq.get(n1)
            freq2 = freq.get(n2)
            if (freq1 != freq2): 
                return freq1 - freq2
            else: 
                return n2 - n1 
            
        return sorted(nums, key=cmp_to_key(sortfunc))