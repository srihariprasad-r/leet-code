class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        end = defaultdict(list)

        for num in nums:
            if num-1 not in end:
                heapq.heappush(end[num], 1)
            else:
                if end[num-1]:
                    el = heapq.heappop(end[num-1])
                # this is needed
                if len(end[num-1]) == 0:
                    del end[num-1]
                heapq.heappush(end[num], el+1)

        for k, v in end.items():
            if len(v) > 0 and v[0] < 3:
                return False

        return True
