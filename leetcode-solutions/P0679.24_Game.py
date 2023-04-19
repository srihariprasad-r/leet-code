# wrong submission

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        seen = set()
        q = deque()
        q.append(cards)

        lst = ['+', '-', '*', '/']

        while q:
            items = q.popleft()
            op = []

            if len(items) == 1:
                return True if 23.99 < abs(items[-1]) < 24 else False

            seen.add(tuple(items))

            for i in range(len(items)):
                el = items[:i] + items[i+1:]
                for j in range(len(el)):
                    x = items[i]
                    y = el[j]
                    nxt = el[:j] + el[j+1:]
                    for l in lst:
                        if l == '+':
                            op.append((x + y))
                        if l == '-':
                            op.append((x - y))
                            op.append((y - x))
                        if l == '*':
                            op.append((x * y))
                        if l == '/' and y != 0:
                            op.append((x / y))
                        if l == '/' and x != 0:
                            op.append((y / x))

                    for o in op:
                        if tuple(nxt + [o]) not in seen:
                            q.append(nxt + [o])
                            seen.add(tuple(nxt + [o]))

        return False