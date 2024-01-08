class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)
        visited = [0] * len(isConnected)
        c = 0

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        def dfs(n):
            if n >= len(isConnected): return

            for i in adj_list[n]:
                if visited[i] != 1: 
                    visited[i] = 1
                    dfs(i)

            return
        
        for i in range(len(isConnected)):
            if not visited[i]:
                visited[i] = 1
                dfs(i)
                c += 1

        return c