class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        mp = {
            2 : ['abc'],
            3 : ['def'],
            4 : ['ghi'],
            5 : ['jkl'],
            6 : ['mno'],
            7 : ['pqrs'],
            8 : ['tuv'],
            9 : ['wxyz'],
        }

        res = []
        def recursion(idx, strg):
            if idx == len(digits):
                res.append(strg)
                return

            s = mp[int(digits[idx])]
            for c in ''.join(s):
                recursion(idx+1, strg + c)

            return res

        return recursion(0, '')