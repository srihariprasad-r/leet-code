class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        mxleft = [0] * (len(height)+1)
        mxright = [0] * (len(height)+1)

        for i in range(len(height)):
            mxleft[i] = max(mxleft[i-1], height[i])

        for i in range(len(height)-1, -1, -1):
            mxright[i] = max(mxright[i+1], height[i])

        for i in range(len(height)):
            t = min(mxleft[i], mxright[i])
            if t >= height[i]:
                res += t - height[i]

        return res