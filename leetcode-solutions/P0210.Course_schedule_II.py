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
    
# Method 2 - Topological sort

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
                    if recursion(adj[n][i]):
                        return True

            visited[n] = 1
            return False

        for i in range(numCourses):
            if recursion(i):
                return []

        visited = [False] * numCourses
        stck = []

        def tpsort(n, stck):
            visited[n] = True

            for x in adj[n]:
                if not visited[x]:
                    tpsort(x, stck)

            stck.append(n)
            return stck

        for i in range(numCourses):
            if not visited[i]:
                tpsort(i, stck)

        return stck

# Method 3
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0] * (numCourses+1)
        path = [0] * (numCourses+1)
        stck = []
        lst = collections.defaultdict(list)

        for i in range(len(prerequisites)): 
            lst[prerequisites[i][0]].append(prerequisites[i][1])       

        def dfs(node):
            visited[node] = 1
            path[node] = 1

            for n in lst[node]:
                if not visited[n]:
                    if dfs(n): return True
                elif path[n]: return True

            path[node] = 0
            stck.append(node)

            return False

        hasCycle = True
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return []
        
        return stck