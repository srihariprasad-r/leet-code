# wrong submission

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        lst = collections.defaultdict(list)
        q = deque()
        ans = 0
        indegree = [0] * (n+1)

        for e in relations:
            indegree[e[1]] += 1
            lst[e[0]].append(e[1])

        for idx, val in enumerate(indegree):
            if indegree[idx] == 0:
                q.append((val))

        while q:
            course = q.popleft()

            for c in lst[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

            ans += 1

        return ans