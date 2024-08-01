class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k: return False

        need = s // k
        
        def recursion(idx, st, s_k):
            if idx >= len(nums): return

            if st == 0 or s_k == 0: return True

            st += nums[idx]
            if st == need: 
                return recursion(idx+1, 0, s_k - 1)

            for i in range(idx, len(nums)):
                if st < need :
                    if recursion(i+1, st, s_k):
                        return True

            return False

        return recursion(0, 0, k)

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k: return False

        need = s // k

        def recursion(idx, st, s_k):
            if idx >= len(nums): return False
            
            if idx == len(nums) - 1 and st + nums[idx] == need: 
                return True

            if st == need:
                return recursion(idx+1, 0, s_k + 1)

            if s_k == k:
                return True

            take = False
            if st + nums[idx] <= need:
                st += nums[idx]
                take = recursion(idx+1, st, s_k+1)
            else:
                take = recursion(idx+1, 0, s_k)
            #no_take = recursion(idx+1, st, s_k)

            return take

        return recursion(0, 0, 0)        