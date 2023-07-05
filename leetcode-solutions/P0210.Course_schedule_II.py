class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        ans = []
        indegree = [0] * (numCourses)
        for e, v in prerequisites:
            graph[v].append(e)
            indegree[e] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            for _ in range(len(q)):
                cur = q.pop()
                ans.append(cur)

                for e in graph[cur]:
                    indegree[e] -= 1
                    if indegree[e] == 0:
                        q.append(e)

        return ans if len(ans) == numCourses else []
    
# wrong submission

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)

        for x in prerequisites:
            adj[x[0]].append(x[1])

        visited = [0] * numCourses 

        def recursion(n):
            if visited[n] == 2:
                return True

            visited[n] = 2
            for i in range(len(adj[n])):
                if visited[adj[n][i]] != 1:
                    if recursion(adj[n][i]): return True

            visited[n] = 1

            return False

        for i in range(numCourses):
            if recursion(i):
                return []

        visited = [False] * numCourses 
        stck = []

        def tpsort(n):
            visited[n] = True

            for x in adj[n]:
                if not visited[n]: tpsort(x)
            
            stck.append(n)

            return 

        for i in range(numCourses):
            if not visited[i]:
                tpsort(i)

        return stck