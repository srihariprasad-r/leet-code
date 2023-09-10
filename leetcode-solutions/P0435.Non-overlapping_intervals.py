class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[1])
        x = intervals[0][1]
        cnt = 1

        for intr in intervals:
            if intr[0] >= x:
                cnt += 1
                x = intr[1]

        return len(intervals) - cnt