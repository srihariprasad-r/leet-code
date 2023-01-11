# TLE submission

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = []

        def dfs(s, fq):
            if len(s) == len(nums):
                ans.append(copy.deepcopy(s))
                return

            for i in range(len(nums)):
                if fq[nums[i]]:
                    s.append(nums[i])
                    fq[nums[i]] -= 1
                    dfs(s, fq)
                    s.pop()
                    fq[nums[i]] += 1

            return ans

        fq = Counter(nums)
        permutations = dfs([], fq)

        mx = float('-inf')
        for i in range(len(permutations)):
            mx = max(
                mx, int(''.join(list(map(lambda x: str(x), permutations[i])))))

        return str(mx)
