# wrong submission

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res =[]

        def dfs(idx, ans):
            if idx > len(num): return 

            if idx == len(num):
                t = ''.join(list(map(lambda x: ''.join(x), ans)))

                if not t[-1].isnumeric(): t = t[:-1]
                if eval(t) > target:
                    return

                if int(eval(t)) == target:
                    if t not in res: res.append(copy.deepcopy(t))
                    return
            else:
                for i in ('*', '-', '+'):
                    tmp = [num[idx]]
                    if idx + 1 < len(num):
                        tmp += i
                    ans.append(tmp)
                    dfs(idx+1, ans)
                    ans.pop()

            return res

        return dfs(0, [])