# wrong submission

class Solution:
    def findPeakGrid(self, arr: List[List[int]]) -> List[int]:
        m = len(arr)
        n = len(arr[0])

        for i in range(len(arr)):
            tmp = [-1]
            tmp.extend(arr[i])
            tmp.append(-1)
            arr[i] = tmp

        l = 0
        h = m * n - 1

        while l <= h:
            mid = l +(h-l)//2
            row = mid // n
            col = mid % n

            if arr[row][col] > arr[row-1][col-1] and arr[row][col] > arr[row-1][col-1]:
                return [row, col]
            
            if arr[row][col] > arr[row-1][col-1]:
                l = mid + 1
            else:
                h = mid - 1