# wrong submission

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        q = []
        visited = set()
        steps = 0
        q.append(beginWord)
        visited.add(beginWord)

        while len(q) > 0:
            el = q.pop(0)
            if el == endWord:
                return steps
            for i in range(len(el)):
                for c in range(26):
                    newstr = ''
                    temp = chr(ord('a') + c)
                    if temp != el[i]:
                        newstr += el[:i]
                        newstr += temp
                        newstr += el[i+1:]
                        if newstr in wordList and newstr not in visited:
                            visited.add(newstr)
                            q.append(newstr)
            steps += 1

        return steps

# TLE

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        visited = set()
        q = [(beginWord, 1)]

        while q:
            el, d = q.pop(0)
            if el == endWord:
                return d
            for i in range(len(el)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newstr = el[:i] + c + el[i+1:]
                    if newstr not in visited and newstr in wordList:
                        visited.add(newstr)
                        q.append((newstr, d + 1))

        return 0
