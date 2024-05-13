# wrong submission
class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        stck = []

        def getmaxidx(arr):
            for i in range(len(arr)):
                while stck and arr[stck[-1]] < arr[i]:
                    stck.pop()
                stck.append(i)

            return stck[0]

        midx = getmaxidx(heights)

        leftsmaller = float('inf')
        stck = []

        for i in range(midx+1):
            while stck and heights[stck[-1]] > heights[i]:
                stck.pop()
            stck.append(i)

        leftsmaller = heights[stck[0]]

        rightsmaller = float('inf')
        stck = []

        for i in range(midx, len(heights)):
            while stck and heights[stck[-1]] > heights[i]:
                stck.pop()
            stck.append(i)

        rightsmaller = heights[stck[0]]     

        s = 0
        i = 0

        while i < len(heights):
            if i == midx:
                s += heights[i]
            elif i < midx:
                s += leftsmaller
            else:
                s += rightsmaller
            i += 1

        return s