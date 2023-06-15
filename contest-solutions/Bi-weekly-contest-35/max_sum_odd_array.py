class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        p = [0]
        ans = 0
        
        for i in range(len(arr)):
            p.append(p[-1] + arr[i])
        
        for i in range(len(p)):
            for j in range(i+1, len(p), 2):
                ans += p[j] - p[i]

        return ans