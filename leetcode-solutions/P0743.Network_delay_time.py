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

# wrong submission
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        lst = collections.defaultdict(list)
        distance = [float('inf')]*(n+1)
        visited = [0]*(n+1)

        for t in times:
            lst[t[0]].append((t[1], t[2]))

        q =  deque()
        q.append((k, 0))
        distance[k] = 0
        visited[k] = 1

        while q:
            node, d = q.popleft()

            for l in lst[node]:
                if visited[l[0]] == 0 and l[1] + d < distance[l[0]]:
                    distance[node] += l[1]
                    q.append((l[0], distance[node]))
                    visited[l[0]] = 1

        return -1 if distance[k] == float('inf') or distance[k] == 0 else distance[k]