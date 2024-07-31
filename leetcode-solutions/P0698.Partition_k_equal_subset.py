class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k: return False
        per_subset = s // k

        d = collections.defaultdict(int)

        cnt = 0
        for n in nums:            
            d[n] = abs(n-per_subset)

        for n in nums:
            if abs(per_subset - n) in d:
                cnt += 1

        return True if cnt >= k else False        