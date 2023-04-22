# wrong submission

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        q = deque([(beginWord, beginWord)])
        seen = set()
        res = []
        ans = defaultdict(set)

        while q:
            n = len(q)
            for _ in range(n):
                parent, cur = q.popleft()
                seen.add((parent, cur))
                if cur == endWord:
                    ans[parent].add(cur)
                    break

                for i in range(len(cur)):
                    first = cur[:i]
                    last = cur[i+1:]
                    t = ''
                    for x in 'abcdefghijklmnopqrstuvwxyz':
                        t = first + x + last
                        if (cur,t) not in seen and t in wordList:
                            q.append((cur, t))
                            seen.add((cur, t))
                            if cur != parent and cur not in ans.keys(): ans[parent].add(cur)
   
        def recurse(ans, key, arr=[]):
            if key not in ans.keys() and key == endWord:
                res.append(arr)
            for k, v in ans.items():
                if k == key:
                    val = list(ans[k])
                    for i in range(len(val)):
                        recurse(ans, val[i], arr + [val[i]])

            return res

        return recurse(ans, beginWord, [beginWord])