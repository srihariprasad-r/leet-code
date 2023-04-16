# wrong submission

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        res = []
        a = set()

        def recursion(idx, val, arr):
            if idx >= len(expression):
                res.append(copy.deepcopy(arr))
                return

            if expression[idx] == '{' or expression[idx] == ',':
                recursion(idx+1, val, arr)
            elif expression[idx] == '}':
                if len(val) > 0:
                    arr.append(val)
                recursion(idx+1, '', arr)
            else:
                recursion(idx+1, val + expression[idx], arr)

            return res

        res = recursion(0, '', [])
        for r in res:
            a |= set(map(''.join, itertools.product(*r)))

        return sorted(a)