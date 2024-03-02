class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        s = 0
        ans = 0

        import collections
        d = collections.defaultdict(int)

        for c in nums:
            if c % 2: s += 1

            d[s] += 1

            if s == k: 
                ans += 1

            if s - k in d:
                ans += d[s-k]

        return ans