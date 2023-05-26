class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def traverse(s, path):
            path.append(s)

            if s == len(graph) - 1:
                res.append(copy.deepcopy(path))

            for v in graph[s]:
                traverse(v, path)

            path.pop()

        traverse(0, [])
        return res