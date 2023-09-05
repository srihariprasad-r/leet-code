class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        q = deque()
        graph = defaultdict(list)
        indeg = [0] * n

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indeg[a] += 1
            indeg[b] += 1

        for i in range(0, n):
            if indeg[i] == 1:
                q.append(i)

        while q:
            ans = []
            for _ in range(len(q)):
                curr = q.popleft()
                ans.append(curr)
                for neighbor in graph[curr]:
                    indeg[neighbor] -= 1
                    if indeg[neighbor] == 1: q.append(neighbor)

        return ans