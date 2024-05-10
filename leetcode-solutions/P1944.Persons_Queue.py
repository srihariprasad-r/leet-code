class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stck = [0]
        res = [0] * len(heights)

        for i in range(1, len(heights)):
            c = 0
            while stck and heights[stck[-1]] < heights[i]:
                j = stck.pop()
                res[j] += 1
            if stck:
                res[stck[-1]] += 1
            stck.append(i)

        return res

# wrong submission
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stck = []
        nge = [0] * len(heights)

        for i in range(len(heights)-1, -1, -1):
            cnt = 1 if i < len(heights) - 1 else 0
            while stck and stck[-1] < len(heights) - 1 and heights[stck[-1]] < heights[i]:              
                stck.pop()
                cnt += 1
            stck.append(i)
            nge[i] += cnt

        return nge        