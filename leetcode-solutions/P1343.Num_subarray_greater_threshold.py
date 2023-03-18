class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        c = sum(arr[:k-1])
        for i in range(len(arr)-k+1):
            c += arr[k+i-1]
            if c / k >= threshold:
                ans += 1
            c -= arr[i]

        return ans
