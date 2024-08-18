class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        newlist = []
        for i in range(len(startTime)):
            newlist.append((startTime[i],endTime[i],profit[i]))

        def nextidx(lst, idx):       
            l = 0
            r = len(lst) - 1

            res = len(lst)

            while l <= r:
                mid =  l + (r-l)//2

                if lst[idx][1] <= lst[mid][0]:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1

            return res

        def recursion(idx, c):
            if idx >= len(newlist): return c

            new_idx = nextidx(newlist, idx)
            include = recursion(new_idx, c + newlist[idx][2])
            exclude = recursion(idx+1, c)

            return max(include, exclude)
        
        return recursion(0, 0)