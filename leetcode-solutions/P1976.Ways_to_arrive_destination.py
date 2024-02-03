# wrong submission
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        lst = collections.defaultdict(list)
        distance = [float('inf')] *(n)
        t = [0] * n

        for l in roads:
            lst[l[0]].append((l[1], l[2]))
            lst[l[1]].append((l[0], l[2]))

        q = []
        q.append((0,0))
        heapq.heapify(q)
        distance[0] = 0
        t[0] = 1

        while q:
            d, node = heapq.heappop(q)

            for l in lst[node]:
                if d  + l[1] < distance[l[0]]:
                    distance[l[0]] = d + l[1]
                    heapq.heappush(q,(d+l[1],l[0]))
                    t[l[0]] = t[node]
                elif d + l[1] == distance[l[0]]:
                    t[l[0]] += t[node]

        return t[n-1]