class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        @lru_cache(None)
        def dp(node, c):
            if node == n - 1:
                return passingFees[n-1]

            ans = float('inf')

            for (v, t) in graph[node]:
                if c + t <= maxTime:
                    ans = min(ans, passingFees[node] + dp(v, c + t))

            return ans

        graph = defaultdict(list)

        n = len(passingFees)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        ans = dp(0, 0)

        return -1 if ans == float('inf') else ans
