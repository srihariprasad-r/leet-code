class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        presum = [0]
        dct = {0:-1}
        ans = float('inf')

        for x in nums:
            presum.append(presum[-1] + x)
            
        sm = presum[-1] % p

        for i, el in enumerate(presum):
            dct[el%p] = i
            rem = ((el%p - sm) % p + p ) % p
            if rem in dct:
                ans = min(ans, i - dct[rem])

        return ans if ans != float('inf') else -1