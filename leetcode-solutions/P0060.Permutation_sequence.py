# TLE

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(fq, arr, res):
            if len(arr) == n:
                if arr not in res: res.append(copy.deepcopy(arr))
                return

            for num in nums:
                if not fq[int(num)-1]:
                    fq[int(num)-1] = True
                    arr.append(num)
                    dfs(fq, arr, res)
                    arr.pop()
                    fq[int(num)-1] = False
            
            return res

        nums = [str(i) for i in range(1, n+1)]
        fq = [False] * len(nums)
        res = dfs(fq, [], [])

        cnt = 0
        for m in res:
            if cnt == k-1:
                return ''.join(res[cnt])
            cnt += 1