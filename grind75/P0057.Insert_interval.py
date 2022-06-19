class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        stck = []

        for i in range(len(intervals)):
            # newInternal goes before current interval
            if newInterval[1] < intervals[i][0]:
                stck.append(newInterval)
                return stck + intervals[i:]
            # newInterval goes after, but may overlap so do not push newInterval now
            elif newInterval[0] > intervals[i][1]:
                stck.append(intervals[i])
            else:
                # overlapping intervals
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]

        stck.append(newInterval)

        return stck