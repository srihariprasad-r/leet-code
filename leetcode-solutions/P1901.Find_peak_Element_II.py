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

# wrong submission
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        r = len(mat)
        c = len(mat[0])

        def bs(arr):
            if len(arr) == 2: return 0 if arr[0] > arr[1] else 1
            l = 0
            r = len(arr)-1

            while l < r:
                mid = l + (r-l) // 2
                
                if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                    return mid

                if arr[mid-1] < arr[mid] and arr[mid] < arr[mid+1]:
                    l = mid + 1
                else:
                    r = mid 

            return l if arr[l] > arr[r] else r

        mxval = float('-inf')
        o_idx = []
        for r in range(len(mat)):
            midx = bs(mat[r])
            v = mat[r][midx]
            if v > mxval:
                o_idx = [r, midx]
                mxval = v

        return o_idx