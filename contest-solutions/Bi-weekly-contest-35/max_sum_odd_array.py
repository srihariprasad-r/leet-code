# wrong submission

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        self.ans = 0
        def recursion(idx, s, res):
            if idx == len(arr):
                if len(res) % 2 == 1:
                    self.ans += s
                return
            
            res.append(arr[idx])
            recursion(idx+1, s + arr[idx], res)
            res.pop()
            
            return self.ans
        
        return recursion(0, 0, [])