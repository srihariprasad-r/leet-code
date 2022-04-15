class Solution(object):
    def kSimilarity(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        queue = deque()
        ans = 0

        visited = set()
        visited.add(s1)

        n = len(s1)

        queue.append(s1)

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()

                if cur == s2:
                    return ans

                i = 0
                curList = list(cur)

                while i < len(curList):
                    if curList[i] == s2[i]:
                        i += 1
                    else:
                        break

                for j in range(i, n):
                    if s2[j] != curList[j] and s2[i] == curList[j]:
                        curList[i], curList[j] = curList[j], curList[i]

                        el = ''.join(curList)
                        if el not in visited:
                            visited.add(el)
                            queue.append(el)

                        curList[i], curList[j] = curList[j], curList[i]

            ans += 1

        return ans
