# wrong submission

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        if not relations:
            if n % k == 0:
                return n // k
            else: return n // k + 1

        lst = collections.defaultdict(list)
        q = deque()
        v = 0
        ans = 0
        indegree = [0] * (n+1)

        for e in relations:
            indegree[e[1]] += 1
            lst[e[0]].append(e[1])

        for idx, val in enumerate(indegree):
            if indegree[idx] == 0:
                q.append(val)

        while q:
            course = q.popleft()
            while v < k:
                for c in lst[course]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        q.append(c)

                v += 1

            v = 0
            ans += 1


        return ans