class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        start = headID
        self.t = 0

        visited = [0]* len(manager)
        adjlist = collections.defaultdict(list)

        for idx, el in enumerate(manager):
            # if el == -1: continue
            adjlist[el].append(idx)

        def dfs(idx, tme):
            visited[idx] = 1

            for v in adjlist[idx]:
                if not visited[v]:     
                    self.t = max(self.t, tme + informTime[v])                                   
                    dfs(v, tme + informTime[v])
            
            return self.t

        return dfs(start, informTime[start])        