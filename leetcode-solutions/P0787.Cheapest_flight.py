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