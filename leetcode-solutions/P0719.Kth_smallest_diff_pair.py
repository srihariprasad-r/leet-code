# TLE
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        q = []
        res = []
        import copy

        def combinations(idx, r, cnt):
            if cnt == 2: 
                res.append(copy.deepcopy(r))
                return
                
            for i in range(idx, len(nums)):
                r.append(nums[i])
                combinations(i+1, r, cnt + 1)
                r.pop()

            return res

        c_arr = combinations(0, [], 0)

        heapq.heapify(q)
        
        for i in range(len(c_arr)):
            diff = abs(c_arr[i][0]- c_arr[i][1])
            heapq.heappush(q, diff)

        c = 1
        while c < k:
            heapq.heappop(q)
            c += 1

        return heapq.heappop(q)