class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mx = 0
        cnt = 0

        for i in range(len(arr)):
            if arr[i] > mx:
                mx = arr[i]

            if i == mx:
                cnt += 1

        return cnt

# wromg submission
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stck = []
        cnt = 0

        for i in range(len(arr)):
            while stck and stck[-1] > arr[i]:
                cnt += 1
                stck.pop()
            stck.append(arr[i])
        
        return len(arr) - cnt