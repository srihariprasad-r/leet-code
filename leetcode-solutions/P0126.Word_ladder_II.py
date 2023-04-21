# wrong submission

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        q = deque([(beginWord, beginWord)])
        seen = set()
        res = defaultdict(list)
        ans = defaultdict(set)

        while q:
            n = len(q)
            for _ in range(n):
                parent, cur = q.popleft()
                seen.add((parent, cur))
                if cur == endWord:
                    ans[parent].add(cur)
                    # ans = defaultdict(set)
                    break

                for i in range(len(cur)):
                    first = cur[:i]
                    last = cur[i+1:]
                    t = ''
                    for x in 'abcdefghijklmnopqrstuvwxyz':
                        t = first + x + last
                        if (cur, t) not in seen and t in wordList:
                            q.append((cur, t))
                            seen.add((cur, t))
                            if cur != parent and cur not in ans.keys():
                                ans[parent].add(cur)

        print(ans)

        for k, v in ans.items():
            st = list(v)
            for i in range(len(st)):
                res[k].append(st[i])
                if st[i] in ans.keys():
                    val = list(ans[st[i]])
                    for j in range(len(val)):
                        res[k].append(val[j])

        print(res)