class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        end = defaultdict(list)

        for num in nums:
            if num-1 not in end:
                heapq.heappush(end[num], 1)
            else:
                if end[num-1]:
                    el = heapq.heappop(end[num-1])
                # this is needed
                if len(end[num-1]) == 0:
                    del end[num-1]
                heapq.heappush(end[num], el+1)

        for k, v in end.items():
            if len(v) > 0 and v[0] < 3:
                return False

        return True

# Method 2
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = collections.Counter(nums)
        end = collections.Counter()
        
        for num in nums:
            if cnt[num]:
                cnt[num] -= 1
                
                # verify is previous number is available, change it to current number
                if end[num-1]:
                    end[num-1] -= 1
                    end[num] += 1
                # start new subsequence with current and check + 1/+2 are available
                elif cnt[num+1] and cnt[num+2]:
                    cnt[num+1] -= 1
                    cnt[num+2] -= 1
                    end[num+2] += 1
                else:
                    return False
                
        return True