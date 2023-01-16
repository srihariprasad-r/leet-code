# wrong submission

class Solution:
    def decodeString(self, s: str) -> str:
        stck = []
        idx = 0
        n = 0
        for c in s:
            if c == '[':
                stck.append(c)
            elif c == ']':
                el = ''
                while stck[-1] != '[':
                    el += stck.pop()
                stck.pop()
                n = stck.pop()
                stck.append(int(n) * el[::-1])
            else:
                if c.isdigit():
                    if idx >= 1 and s[idx - 1].isdigit():
                        n = n * 10 + int(c)
                        if stck and stck[-1].isdigit():
                            stck.pop()
                        stck.append(str(n))
                    else:
                        n = int(c)
                        stck.append(c)
                else:
                    stck.append(c)
            idx += 1

        return ''.join(stck)
