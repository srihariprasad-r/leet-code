class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def diff_array(arr):
            prev = abs(arr[0] - arr[1])
            for i in range(1,len(arr)-1):
                j = i + 1
                if not(abs(arr[i]-arr[j]) == prev):
                    return False

            return True

        def check_if_arithmentic(arr):
            cnt = 0

            for i in range(len(arr)):
                if diff_array(arr[i]):
                    cnt += 1

            return cnt

        o = []

        def recursion(idx, r=[]):    
            if idx >= len(nums): 
                if len(r) >= 3: o.append(copy.deepcopy(r))
                return 

            r.append(nums[idx])
            recursion(idx+1, r) 
            r.pop()
            recursion(idx+1, r) 
  
            return o

        possible_subsequences = recursion(0, [])
        return check_if_arithmentic(possible_subsequences)