class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        st, csum = 0, 0
        mins = [float('inf')] * len(arr)
        val = float('inf')

        for cur in range(len(arr)):
            csum += arr[cur]

            while st <= cur and csum > target:
                csum -= arr[st]
                st += 1

            if csum == target:
                if st > 0 and mins[st-1] != float('inf'):
                    val = min(val, mins[st-1] + cur - st + 1)
            mins[cur] = min(mins[cur-1], cur - st +
                            1 if csum == target else float('inf'))

        return val if val != float('inf') else -1