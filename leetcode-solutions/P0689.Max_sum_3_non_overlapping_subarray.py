# wrong submission
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        q = []
        heapq.heapify(q)

        c = 0
        ans = 0

        def kadane(a):
            csum = a[0]
            msum = [0]*len(a)
            msum[0] = a[0]

            for i in range(1,len(a)):
                if csum + a[i] > a[i]:
                    csum += a[i]
                else:
                    csum = a[i]

                msum[i] = csum

            return msum
        
        for i in range(len(nums)-k):
            exactK = nums[i]
            s_idx = i            
            j = i + 1
            while j - i < k:
                exactK += nums[j]
                j += 1
            heapq.heappush(q, (s_idx, exactK))

        last_picked_idx = []
        cs = -1
        while q:
            idx, s = heapq.heappop(q)    
            if s > cs:
                if last_picked_idx:
                    if abs(idx - last_picked_idx[-1]) >= k:
                        c += 1
                        last_picked_idx.append(idx)
                        cs = s
                else: 
                    last_picked_idx.append(idx)
                    c += 1
            else:
                continue

        return last_picked_idx
    
# wrong submission
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ms = 0
        ans = [] 

        pleft = [0] * len(nums)
        pright = [len(nums)-k] * len(nums)

        p = [0] * len(nums)
        p[0] = nums[0]

        for i in range(1, len(nums)):
            p[i] = p[i-1] + nums[i]

        total = nums[k] - nums[0]
        for i in range(k, len(nums)):
            s = nums[i-k] - nums[i]
            if s > total:
                total = s
                pleft[i] = i - k
            else:
                pleft[i] = pleft[i-1]

        total = nums[len(nums)-1] - nums[len(nums)-1-k]
        for i in range(len(nums)-k-1, -1, -1):
            s = nums[i+k] - nums[i]
            if s >= total:
                total = s
                pright[i] = i + k
            else:
                pright[i] = pright[i+1]

        for i in range(k, len(nums)-(2*k)):
            l = pleft[i-1]
            r = pright[i+k]
            total = nums[i+k] - nums[i] + nums[l+k] - nums[l] + nums[r+k] - nums[r]
            if total >= ms:
                ans = [l, i, r]
                ms = total

        return ans