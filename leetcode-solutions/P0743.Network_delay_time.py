class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        visited = set()
        time = 0

        for u, v, w in times:
            adj[u].append((v, w))

        q = [(0, k)]
        # heapq.heapify(q)

        while q and len(visited) < n:
            w1, n1 = heapq.heappop(q)
            visited.add(n1)
            time = max(time, w1)

            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(q, (w1 + w2, n2))

        return time if len(visited) == n else -1