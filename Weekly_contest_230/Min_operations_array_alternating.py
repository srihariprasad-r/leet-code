# wrong submission, needs rework

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd_map, even_map = {}, {}
        max_v_odd, max_v_even = -float('inf'),  -float('inf')
        second_flag = False
        
        for i in range(len(nums)):
            if i % 2 == 0:
                if not(nums[i] in even_map):
                    even_map[nums[i]] = 1
                else:
                    even_map[nums[i]] += 1
            else:
                if not(nums[i] in odd_map):
                    odd_map[nums[i]] = 1
                else:
                    odd_map[nums[i]] += 1                
        
        max_v_odd = max([v for v in odd_map.values()])
        max_v_even = max([v for v in even_map.values()])
        
        if max_v_odd == max_v_even:
            second_flag = True
            new_even_map = {k:v for k, v in even_map.items() if v != max_v_even}
            new_v_even = max([v for v in new_even_map.values()])
            
        return len(nums) - max(max_v_odd + new_v_even, new_v_even + max_v_even) if second_flag else len(nums) - (max_v_odd + max_v_even)