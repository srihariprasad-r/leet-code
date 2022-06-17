class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])

        if not mat:
            return None

        nums = [[] for _ in range(m+n-1)]
        ans = []

        for i in range(m):
            for j in range(n):
                nums[i+j].append(mat[i][j])

        for i in range(m+n-1):
            if i % 2 == 0:
                ans.extend(nums[i][::-1])
            else:
                ans.extend(nums[i])

        return ans
