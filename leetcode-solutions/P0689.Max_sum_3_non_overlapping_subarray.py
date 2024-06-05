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

        p = [0] * (len(nums)+1)

        for i in range(1, len(nums)):
            p[i+1] = p[i] + nums[i-1]

        total = p[k] - p[0]
        for i in range(k, len(nums)):
            s = p[i+1] - p[i+1-k]
            if s > total:
                total = s
                pleft[i] = i - k+1
            else:
                pleft[i] = pleft[i-1]

        total = p[len(nums)] - p[len(nums)-k]
        for i in range(len(nums)-k-1, -1, -1):
            s = p[i+k] - p[i]
            if s >= total:
                total = s
                pright[i] = i
            else:
                pright[i] = pright[i+1]

        for i in range(k, (len(nums)-2*k+1)):
            l = pleft[i-1]
            r = pright[i+k]
            total = p[i+k] - p[i] + p[l+k] - p[l] + p[r+k] - p[r]
            if total >= ms:
                ans = [l, i, r]
                ms = total

        return ans