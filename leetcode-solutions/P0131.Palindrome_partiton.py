class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(st):
            i = 0
            j = len(st) - 1

            while i < j:
                if st[i] != st[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        def recurse(idx, tmp):
            if idx >= len(s): 
                if tmp and not(tmp in res): res.append(copy.deepcopy(tmp))
                return 

            for i in range(idx, len(s)):
                if is_palindrome(s[idx:i+1]):
                    tmp.append(s[idx:i+1])
                    recurse(i+1, tmp)
                    tmp.pop()

            return res
        
        return recurse(0, [])            