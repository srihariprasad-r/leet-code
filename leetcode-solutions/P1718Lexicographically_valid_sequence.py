class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        visited = set()

        def backtrack(idx):
            if idx == el:
                return True

            if ans[idx] != 0:
                return backtrack(idx+1)
            else:
                for num in range(n, 0, -1):
                    if num == 1:
                        if num not in visited:
                            ans[idx] = num
                            visited.add(num)
                            if backtrack(idx+1):
                                return True
                            ans[idx] = 0
                            visited.remove(num)
                    else:
                        if num not in visited and idx + num < len(ans) and ans[idx+num] == 0:
                            ans[idx] = ans[idx+num] = num
                            visited.add(num)
                            if backtrack(idx+1):
                                return True
                            ans[idx] = ans[idx+num] = 0
                            visited.remove(num)
            return False

        el = 1 + (n-1) * 2
        ans = [0] * el

        backtrack(0)
        return ans
