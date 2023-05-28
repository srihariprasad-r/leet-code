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