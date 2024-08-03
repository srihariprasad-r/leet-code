class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:    
        def store_only_max_min_range(arr):
            o = []
            mx, mn = float('-inf'), float('inf')
            for i in range(len(arr)):
                mx = max(arr[i]) 
                mn = min(arr[i])
                if mx - mn <= k:
                    o.append(arr[i])
            return o

        def recursion(idx,s, o=[], r=[]):            
            if s == 0: 
                r.append(copy.deepcopy(o))
                return

            if idx >= len(nums):  return r

            for i in range(idx, len(nums)):
                o.append(nums[i])    
                recursion(i+1, s - 1, o, r)
                o.pop()

            return r

        cnt = 0
        for i in range(1,len(nums)):
            k_size = i
            left_over_k_size = len(nums) - i
            res_left = recursion(0, k_size, [], [])
            res_right = recursion(0, left_over_k_size, [], [])
            el_left = store_only_max_min_range(res_left) 
            el_right = store_only_max_min_range(res_right) 
            if el_left  and el_right: 
                cnt += 1

        return cnt