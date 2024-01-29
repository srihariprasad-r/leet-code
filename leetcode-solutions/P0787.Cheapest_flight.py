# TLE

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dct = collections.defaultdict(list)
        visited = [0] * (len(flights)+1)
        for s in flights:
            dct[s[0]].append((s[1], s[2]))

        if src not in dct.keys(): return -1

        def dfs(src, dct, cost, ans, k,visited):
            if k < 0: return float('inf')

            if src == dst: 
                ans = min(ans,cost)
                return ans

            t = float('inf')
            visited[src] = 1

            for x in dct[src]:
                if not visited[x[0]] and cost + x[1] <= ans:
                    t = min(t, dfs(x[0], dct, cost + x[1], ans , k - 1,visited))
           
                visited[src] = 0

            return t 

        return dfs(src, dct, 0, float('inf') , k+1, visited)

# Method 2
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        lst = collections.defaultdict(list)
        cost = [float('inf')]*(n+1)
        mx = float('inf')

        for f in flights:
            lst[f[0]].append((f[1],f[2]))

        q = deque()
        q.append((src,0, k))
        cost[src] = 0  

        while q:
            node, c, v = q.popleft()
            
            # if node == dst and v == 0: 
            #     return c

            for l in lst[node]:
                if v >= 0 and c + l[1] < cost[l[0]]:
                    q.append((l[0] , l[1]+ c, v - 1))
                    cost[l[0]] = c + l[1]

        return -1 if cost[dst] == float('inf') else cost[dst]