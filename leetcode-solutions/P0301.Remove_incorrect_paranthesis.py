class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(st):
            o = 0

            for i in range(len(st)):
                if o < 0:
                    return False

                if st[i] == '(':
                    o += 1
                elif st[i] == ')':
                    o -= 1
                else:
                    continue

            return o == 0

        q = list()
        res = []
        q.append((0, s))
        visited = set()

        while q:
            for _ in range(len(q)):
                x, cur = q.pop()

                if valid(cur):
                    res.append(cur)

                for i in range(len(cur)):
                    new_str = cur[:i] + cur[i+1:]
                    if len(new_str) > 0:
                        if new_str not in visited:
                            q.append((i, new_str))
                            visited.add(new_str)

        mx = 0
        for i in range(len(res)):
            mx = max(mx, len(res[i]))

        res = list(filter(lambda x: len(x) == mx, res))

        return res if res else [""]