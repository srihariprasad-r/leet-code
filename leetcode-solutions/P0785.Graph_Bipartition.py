class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [-1] * len(graph)

        def dfs(idx, color):
            if visited[idx] != -1: return visited[idx] == color

            visited[idx] = color
            for i in range(len(graph[idx])):
                if not dfs(graph[idx][i], 1-color):
                    return False

            return True

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if visited[graph[i][j]] == -1 and not dfs(graph[i][j], 1):
                    return False

        return True