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

# Method 2

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        graph = defaultdict(list)

        n = len(passingFees)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        fees = [float('inf')] * n
        times = [float('inf')] * n
        fees[0] = passingFees[0]
        times[0] = 0

        q = [(passingFees[0], 0, 0)]

        while q:
            f, time, u = heapq.heappop(q)

            for v, t in graph[u]:
                if time + t <= maxTime and (f+passingFees[v] < fees[v] or time+t < times[v]):
                    heapq.heappush(q, (f+passingFees[v], time+t, v))
                    if f+passingFees[v] < fees[v]:
                        fees[v] = f + passingFees[v]
                    if time+t < times[v]:
                        times[v] = time + t

        return -1 if fees[-1] == float('inf') else fees[-1]
