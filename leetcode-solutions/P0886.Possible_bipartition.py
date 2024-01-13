# wrong submission

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not dislikes: return True
        
        colors = [-1] * (n+1)

        adj = {}

        for d in dislikes:
            if d[0] not in adj:
                adj[d[0]] = [d[1]]
            else:
                adj[d[0]].append(d[1])

            if d[1] not in adj:
                adj[d[1]] = [d[0]]
            else:
                adj[d[1]].append(d[0])

        q = [1]
        colors[1] = 1
        
        while q:
            for _ in range(len(q)):
                el = q.pop()
                for e in adj[el]:
                    if colors[e] == colors[el]:
                        return False
                    if colors[e] == -1:
                        colors[e] = 1 - colors[el]
                        q.append(e)

        return True

# wrong submission
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        lst = collections.defaultdict(list)
        visited = [-1] * (n+1)

        for i in range(len(dislikes)):
            lst[dislikes[i][0]].append(dislikes[i][1])
            lst[dislikes[i][1]].append(dislikes[i][0])

        def dfs(node, color):
            if visited[node] != -1: return visited[node] == color

            visited[node] = color
            for n in lst[node]:
                if dfs(n, 1-color):
                    return True

            return False

        for i in range(1,n+1):
            if visited[i] == -1 and dfs(i, 1):
                return True

        return False