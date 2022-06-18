class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(groupIndex, numIndex):
            if groupIndex == m:
                return True

            if numIndex == n:
                return False

            curGroup = groups[groupIndex]
            # choosing deque since append and pop are O(1) rather list slicing is O(n)
            curNums = deque()
            for i in range(numIndex, n):
                curNums.append(nums[i])
                if len(curNums) > len(curGroup):
                    curNums.popleft()

                if curGroup == list(curNums):
                    # quit when first match to save rest of elements for next grouo compare
                    return dfs(groupIndex+1, i+1)

            return False

        m = len(groups)
        n = len(nums)

        return dfs(0, 0)
