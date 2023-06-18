class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            p = root[x]
            while p != root[p]:
                p = root[p]

            return p

        def union(x, y):
            p1 = find(x)
            p2 = find(y)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                root[p2] = p1
                rank[p1] += rank[p2]
            else:
                root[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]