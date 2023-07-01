class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}

        for t in tickets:
            if (t[0] in adj):
                adj[t[0]].append(t[1])
            else:
                adj[t[0]] = [t[1]]

        for k in adj.keys():
            adj[k].sort(reverse=True)

        stck = ['JFK']
        res = []
        while stck:
            el = stck[-1]
            if el in adj and len(adj[el]) > 0:
                stck.append(adj[el].pop())
            else:
                res.append(stck.pop())

        return res[::-1]