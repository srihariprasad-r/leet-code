class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        visited = [False] * (numCourses)
        self.course = False

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])        

        def traverse(s, path=[]):
            if s in path:
                self.course = True
                return 

            if visited[s]: return

            visited[s] = True
            path.append(s)
            for v in graph[s]:
                traverse(v, path)
                if self.course:
                    break
            path.pop()

        for i in range(numCourses):
            traverse(i)

        return not self.course

# Method 2
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        lst  = collections.defaultdict(list)

        visited = [0] * (numCourses+1)
        path = [0] * (numCourses+1)
        for i in range(len(prerequisites)):
            lst[prerequisites[i][0]].append(prerequisites[i][1])
        
        def dfs(node):
            visited[node] = 1
            path[node] = 1

            for n in lst[node]:
                if not visited[n]:
                    if dfs(n):
                        return True
                elif path[n]:
                    return True

            path[node] = 0

            return False
        
        hascycle = False
        for i in range(numCourses+1):
            if visited[i] == 0:
                if dfs(i):
                    hascycle = True

        return not hascycle 