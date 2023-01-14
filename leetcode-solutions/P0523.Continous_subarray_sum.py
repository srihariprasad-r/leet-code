# wrong submission

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = defaultdict(int)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s % k in mp:
                if i - mp[s % k] > 1:
                    return True
            mp[s % k] = i

        return False