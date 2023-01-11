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

# Method 2

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        def mergesort(nums, l, r):
            if l > r: return []
            if l == r: return [nums[l]]

            mid = l + (r-l) // 2
            left = mergesort(nums, l, mid)
            right = mergesort(nums, mid+1, r)

            return merge(left, right)

        def merge(l, r):
            res = []
            i = 0
            j = 0

            while i < len(l) and j < len(r):
                if str(l[i]) + str(r[j]) > str(r[j]) + str(l[i]):
                    res.append(l[i])
                    i += 1
                else:
                    res.append(r[j])
                    j += 1

            while i < len(l):
                res.append(l[i])
                i += 1

            while j < len(r):
                res.append(r[j])
                j += 1

            return res 

        o = mergesort(nums, 0, n-1)
        return str(int(''.join(map(str, o))))
