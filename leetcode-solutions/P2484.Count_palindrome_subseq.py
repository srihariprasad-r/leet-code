# wrong submission

class Solution:
    def countPalindromes(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for g in range(len(s)):
            j = g
            for i in range(len(s)):
                if g == 0:
                    dp[i][j] = 1
                elif g == 1:
                    if s[i] == s[j]: 
                        dp[i][j] = 3
                    else:
                        dp[i][j] = 2
                else:
                    if g == 4:
                        if s[i] == s[j]:
                            dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
                        else:
                            dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                    
                if j < len(s)-1: 
                    j += 1
                else:
                    break

        return dp[0][4]


class Solution:
    def countPalindromes(self, s: str) -> int:
        res = []
        k = 5

        def palindrome(st):
            i = 0
            j = len(st) - 1

            while i != j:
                if st[i] != st[j]: return False
                i += 1
                j -= 1
            return True

        def recurse(idx, st, res):
            if idx >= len(s): 
                if len(st) == k and palindrome(st): res.append(copy.deepcopy(st))
                return res

            if len(st) < k:
                take = recurse(idx+1, st + s[idx], res)
            
            no_take = recurse(idx+1, st, res)

            return res

        return len(recurse(0, '', res))        