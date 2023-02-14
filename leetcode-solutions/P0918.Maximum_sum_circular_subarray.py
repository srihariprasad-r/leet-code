class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s = 0
        ans = nums[0]

        lst = [(0, -1)]
        heapq.heapify(lst)

        for i in range(2*len(nums)):
            s += nums[i % len(nums)]
            while lst and i - lst[0][1] > len(nums):
                heapq.heappop(lst)
            ans = max(ans, s - lst[0][0])
            heapq.heappush(lst, (s, i))

        return ans

# Method  2
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s = 0
        ans = nums[0]

        q = deque()
        q.append((0, -1))
        
        for i in range(2*len(nums)):
            s += nums[i%len(nums)]
   
            if q and i - q[0][1] > len(nums):
                q.popleft()

            ans = max(ans, s - q[0][0])

            while q and q[-1][0] >= s:
                q.pop()

            q.append((s, i))

        return ans