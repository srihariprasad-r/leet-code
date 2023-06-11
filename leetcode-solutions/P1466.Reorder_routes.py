# TLE

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edge = defaultdict(list)
        neighbours = []
        visited = set()
        i = 0

        for a, b in connections:
            neighbours.append((a,b))

        for a, b in connections:
            edge[a].append(b)
            edge[b].append(a)

        q = deque()
        q.append(0)
        visited.add(0)
        
        while q:
            n1 = q.popleft()

            for e in edge[n1]:
                if e in visited:
                    continue
                if (e, n1) not in neighbours:
                    i += 1
                q.append(e)
                visited.add(e)

        return i