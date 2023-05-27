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