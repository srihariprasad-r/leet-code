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

        need = int(s / k)
        self.groups = 0

        visited = [0] * len(nums)

        def recursion(idx, st, s_k):
            if idx == len(nums) - 1:
                if st + nums[idx] == need: 
                    s_k += 1
                    self.groups += 1
                # if s_k == k: return True
                return False
 
            if st == need: return True

            for i in range(len(nums)):
                if not visited[i] and st + nums[i] <= need:
                    visited[i] = 1
                    st += nums[i]
                    if st == need: 
                        s_k += 1
                        st = 0
                    if recursion(i+1, st, s_k): 
                        self.groups += 1
                        return True
                    st -= nums[i]
                    visited[i] = 0

            return self.groups == k

        return recursion(0, 0, 0)                  