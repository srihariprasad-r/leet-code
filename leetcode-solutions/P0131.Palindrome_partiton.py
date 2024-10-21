class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def palindrome(st):
            i = 0
            j = len(st) - 1

            while i < j:
                if st[i] != st[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        def recurse(i, tmp):
            if i == len(s):       
                if tmp and not(tmp in res): res.append(copy.deepcopy(tmp))
                return           

            for k in range(i, len(s)):         
                if palindrome(s[i:k+1]):
                    tmp.append(s[i:k+1])                          
                    recurse(k+1, tmp)   
                    tmp.pop()             

            return res
        
        return recurse(0, [])                    

