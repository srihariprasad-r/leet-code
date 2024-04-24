# wrong submission
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        d = collections.defaultdict(list)
        ans = [0]*(n)

        for e in edges:
            d[e[0]].append(e[1])

        def dfs(node, parent_label, cnt):     
            for n in d[node]:
                if labels[n] == parent_label:
                    cnt += 1
                dfs(n, labels[n], cnt) 

            return cnt

        for i in range(n):
            ans[i] += dfs(i, labels[i], 1)

        return ans