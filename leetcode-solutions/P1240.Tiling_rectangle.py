class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        def recursion(x, y):
            if x == 0 or y == 0: return 0
            if y > x: x, y = y , x

            if x == 1 or y == 1: return y

            if x == y: return 1

            if not x % y: return x // y

            cnt = 1 + recursion(x, x-y)
            for l1 in range(1, n):
                hztl = 1 + recursion(x-l1, l1) + recursion(x, y-l1)
                vctl = 1 + recursion(l1, y-l1) + recursion(x-l1, y)

                res = min(cnt, min(hztl, vctl))

                for l2 in range(n+1-l1, n):
                    if l1 + l2 >= x: break
                    others = 2 + recursion(x-l1, y -l2) + recursion(x-l2, y-l1) + recursion(x-l1-l2, l1+l2-y)

                    res = min(res, others)

            return res

        return recursion(n, m)