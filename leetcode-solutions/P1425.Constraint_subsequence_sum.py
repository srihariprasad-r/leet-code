class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import deque
        
        arr = nums[:1]
        dec = deque(arr)
        for i, el in enumerate(nums[1:], 1):
            if i > k and dec[0] == arr[i-k-1]:
                dec.popleft()

            maxel = max(el, dec[0] + el)
            arr.append(maxel)
            while dec and dec[-1] < maxel:
                dec.pop()
            
            dec.append(maxel)
            
        return max(arr)

# Method 2
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        deq = deque()
        dp = [0] * len(nums)

        for idx, num in enumerate(nums):
            if idx > k and deq and deq[0] == dp[idx-k-1]:
                deq.popleft()

            dp[idx] = max(deq[0] if deq else 0,0) + num

            while deq and deq[-1] < dp[idx]:
                deq.pop()

            deq.append(dp[idx])

        return max(dp)