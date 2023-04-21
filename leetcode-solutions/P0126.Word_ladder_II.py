# wrong submission

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        q = deque([beginWord])
        seen = set()
        res = []
        ans = []
        while q:
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                seen.add(cur)
                if cur == endWord:
                    res.append(ans)
                    ans = []

                for i in range(len(cur)):
                    first = cur[:i]
                    last = cur[i+1:]
                    t = ''
                    for x in 'abcdefghijklmnopqrstuvwxyz':
                        t = first + x + last
                        if t not in seen and t in wordList:
                            q.append(t)
                            seen.add(t)
                            ans.append(t)
 
        return res