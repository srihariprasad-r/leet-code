class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        pq = []
        res = 0
        d = 0
        idx = 0
        events.sort(key=lambda x: x[0])
        max_day = max([events[i][1] for i in range(len(events))])

        while d <= max_day:
            while pq and pq[0] < d:
                heapq.heappop(pq)

            while idx < len(events) and events[idx][0] == d:
                heapq.heappush(pq, events[idx][1])
                idx += 1

            if pq:
                heapq.heappop(pq)
                res += 1

            d += 1

        return res
