class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        arr = defaultdict(int)
        cnt = 0

        for i in range(len(rectangles)):
            dv = rectangles[i][0]/rectangles[i][1]
            cnt += arr[dv]
            arr[dv] += 1

        return cnt
