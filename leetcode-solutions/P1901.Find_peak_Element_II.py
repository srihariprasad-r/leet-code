class Solution:
    def findPeakGrid(self, arr: List[List[int]]) -> List[int]:
        m = len(arr)
        n = len(arr[0])

        def f(arr, c):
            mx = float('-inf')
            idx = -1
            for i in range(len(arr)):
                if mx < arr[i][c]:
                    mx = arr[i][c]
                    idx = i

            return idx

        l = 0
        h = n - 1

        while l <= h:
            mid = l +(h-l)//2
            mx_idx = f(arr, mid)

            left = arr[mx_idx][mid - 1] if mid >= 1 else -1
            right = arr[mx_idx][mid + 1] if mid + 1 < n else -1 

            if arr[mx_idx][mid] > left and arr[mx_idx][mid] > right:
                return [mx_idx, mid]
            
            if arr[mx_idx][mid] > left:
                l = mid + 1
            else:
                h = mid - 1