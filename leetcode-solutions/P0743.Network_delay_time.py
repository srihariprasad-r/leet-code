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
        mx = float('-inf')
        all_nodes_visited = True
        last_node = 0

        for t in times:
            lst[t[0]].append((t[1], t[2]))

        q =  deque()
        q.append(k)
        distance[k] = 0
        visited[k] = 1

        while q:
            node = q.popleft()
            visited[node] = 1
            last_node = node

            for l in lst[node]:
                if l[1] + distance[node] < distance[l[0]]:
                    distance[l[0]] = l[1] + distance[node]
                    q.append(l[0])
                    visited[l[0]] = 1

        for i in range(1, len(visited)): 
            if visited[i] == 0: all_nodes_visited = False

        for i in range(1, len(distance)): 
            if distance[i] > mx: mx = distance[i]

        return -1 if not all_nodes_visited else mx

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        adjlist = collections.defaultdict(list)
        lst = []

        dst = [float('inf')] * (n+1)

        for i in range(len(times)):
            adjlist[times[i][0]].append((times[i][1], times[i][2]))

        dst[k] = 0

        lst.append((0, k))        

        heapq.heapify(lst)

        while lst:
            top = heapq.heappop(lst)
            node, dist = top[1], top[0]
            for n in adjlist[node]:
                if dist + n[1] < dst[n[0]]:
                    dst[n[0]] = dist + n[1]                  
                    heapq.heappush(lst, (dst[n[0]] , n[0]))
        
        res = -1
        for idx, k in enumerate(dst):
            if idx > 0 and k == float('inf'):
                return -1 
            if k != float('inf') and k > 0:
                res = max(res, k)
        
        return res  