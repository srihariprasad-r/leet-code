# wrong submission
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        lst = collections.defaultdict(list)
        distance = [float('inf')] *(n)
        t = [0] * n

        for l in roads:
            lst[l[0]].append((l[1], l[2]))
            lst[l[1]].append((l[0], l[2]))

        q = deque()
        q.append(0)
        distance[0] = 0
        t[0] = 0

        while q:
            node = q.popleft()

            for l in lst[node]:
                if distance[node]  + l[1] < distance[l[0]]:
                    distance[l[0]] = distance[node] + l[1]
                    q.append(l[0])
                    t[l[0]] = t[node]

                if distance[node]  + l[1] == distance[l[0]]:
                    t[l[0]] += 1

        return t[n-1]%100_000_000