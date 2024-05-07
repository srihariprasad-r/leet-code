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

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stck = []
        cnt = 0
        cmax = 0

        for i in range(len(arr)):
            if not stck or (stck and stck[-1] < arr[i]):
                stck.append(arr[i])
                cmax = arr[i]
            else:
                while stck and stck[-1] > arr[i]:
                    stck.pop()
                stck.append(cmax)
        
        return len(stck)