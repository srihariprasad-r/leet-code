class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        def recursion(idx, s):
            if idx >= len(arr):
                return s
            
            take = recursion(idx+1, max(arr[idx], s + arr[idx]))
            no_take = recursion(idx+1, s)

            return max(take, no_take)

        res = recursion(0,0)
        
        return -1 if res <= 0 else res        