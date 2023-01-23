# wrong submission

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stck = []
        for n in num:
            while stck and int(stck[-1]) > int(n) and k > 0:
                stck.pop()
                k -= 1
            stck.append(n)

        while stck and k > 0:
            stck.pop()
            k -= 1

        idx = 0
        while stck and idx < len(stck) and stck[idx] == '0':
            idx += 1

        return ''.join(stck[idx:]) if len(stck[idx:]) > 0 else '0'
