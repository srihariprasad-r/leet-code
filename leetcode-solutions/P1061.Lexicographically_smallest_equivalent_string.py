class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ans = ''
        def find(x):
            if x == root[x]:
                return x
            else:
                return find(root[x])

        def union(p1, p2):
            x = find(p1)
            y = find(p2)

            if x == y:
                return
            
            if x < y:
                root[y] = x
            else:
                root[x] = y         

            return

        root = [i for i in range(26)]

        for x, y in zip(s1, s2):
            union(ord(x) - ord('a'), ord(y) -ord('a'))

        for c in baseStr:
            ans += chr(find(ord(c)-ord('a'))+ord('a'))

        return ans