class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        dict = [0]* 26
        for ch in S:
            ascii = ord(ch)-ord('a')
            dict[ascii] += 1 
            

        maxfreq = 0
        maxidx = 0
        for i in range(len(dict)):
            if dict[i]> maxfreq: 
                maxfreq = dict[i]
                maxidx = i

        if maxfreq > (len(S)+1)//2 : return ''  
        
        res = ['']*len(S)
        idx = 0
        while dict[maxidx]:
            res[idx] = chr(maxidx+ord('a'))
            idx += 2
            dict[maxidx] -= 1

        for j in range(26):
            while dict[j] > 0:
                if idx >= len(res):
                    idx = 1
                res[idx] = chr(j+ord('a'))
                idx += 2
                dict[j] -= 1

        return ''.join(res) if len(res) > 0 else ''

# Method2

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = defaultdict(int)
        hp = []
        res = ''
        prev = []

        for el in s:
            c[el] += 1

        for el, o in c.items():
            hp.append((-o, el))

        heapq.heapify(hp)

        while hp:
            cnt, el = heapq.heappop(hp)

            res += el
            cnt += 1

            if prev: 
                heapq.heappush(hp, prev)
                prev = None

            if cnt != 0:
                prev = (cnt, el)

        
        return res if len(res) == len(s) else ''