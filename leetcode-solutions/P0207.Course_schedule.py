# wrong submission

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        self.course = True

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        def traverse(s, path=[]):
            if s in path:
                self.course = False
                return

            path.append(s)
            for v in graph[s]:
                traverse(v, path)
                if self.course:
                    break
            path.pop()

        for i in range(numCourses):
            traverse(i)
        return self.course