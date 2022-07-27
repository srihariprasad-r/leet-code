class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        n = len(intervals)

        sstarts = {interval[0]: i for i, interval in enumerate(intervals)}
        sortedlist = sorted([interval[0] for interval in intervals])

        for st, end in intervals:
            idx = bisect_left(sortedlist, end)

            if idx >= n:
                ans.append(-1)
            else:
                start = sortedlist[idx]
                ans.append(sstarts[start])

        return ans
