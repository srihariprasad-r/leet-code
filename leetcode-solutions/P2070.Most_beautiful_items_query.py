# wrong submission
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        import heapq

        qp = []
        ans = []

        heapq.heapify(qp)

        for idx, e in enumerate(queries):
            heapq.heappush(qp, (e, idx))

        items = sorted(items, key=lambda x:x[0])
        queries = sorted(queries, key = lambda x:x)
        
        for _ in range(len(qp)):
            el, idx = heapq.heappop(qp)
            i = 0
            mx = 0
            while i < len(items) and items[i][0] <= el:
                mx = max(mx, items[i][1])
                i += 1

            ans.append(mx)

        return ans