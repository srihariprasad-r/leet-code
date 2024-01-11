# wrong submission

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        lst = collections.defaultdict(list)
        visited = [-1] * len(graph)

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                lst[i].append(graph[i][j])


        def dfs(idx, color):
            if idx >= len(graph):
                return

            if visited[idx] != -1: return

            visited[idx] = not color
            if idx in lst:
                for i in range(len(lst[i])):
                    if visited[i] != -1:
                        dfs(i, not color)

                    if visited[i] == visited[idx]:
                        return True

            return False

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if visited[j] != -1 and dfs(j, 0):
                    return True

        return False