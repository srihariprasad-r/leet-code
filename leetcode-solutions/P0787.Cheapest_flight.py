# wrong submission

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dct = collections.defaultdict(list)

        for s in flights:
            dct[s[0]].append((s[1], s[2]))

        def dfs(src, dct, cost, ans, k):
            if k < 0:
                return float('inf')

            if src == dst:
                ans = min(ans, cost)
                return ans

            t = float('inf')

            for x in dct[src]:
                t = min(t, dfs(x[0], dct, cost + x[1], ans, k - 1))

            return t

        return dfs(0, dct, s, float('inf'), k+1)