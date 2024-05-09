# wrong submission
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stck = []
        st = set()

        import collections
        d = collections.defaultdict(int)

        for i in range(len(s)):
            d[s[i]] += 1

        for i in range(len(s)):
            while stck and ord(str(stck[-1])) > ord(s[i]) and d[stck[-1]] >= 1:
                st.remove(stck[-1])                
                stck.pop()                            
            if s[i] not in st:
                stck.append(s[i])
                d[s[i]] -= 1    
                st.add(s[i])     

        return ''.join(stck)