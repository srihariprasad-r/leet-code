class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right-left)//2

            bucket = 1
            count = 0

            for w in weights:
                if count + w <= mid:
                    count += w
                else:
                    bucket += 1
                    count = w

            if bucket > days:
                left = mid + 1
            else:
                right = mid

        return right
