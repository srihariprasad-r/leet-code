# Wrong submission

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        ans = {}
        visited = []
        for i in range(len(strs)):
            j = i + 1
            ans[strs[i]] = [strs[i]]
            while j < len(strs):
                mp = Counter(strs[i])
                for c in strs[j]:
                    if c in mp:
                        mp[c] -= 1
                        if not mp[c]:
                            del mp[c]
                    if not mp and not(strs[j] in visited):
                        visited.append(strs[j])
                        lst = ans[strs[i]]
                        lst.append(strs[j])
                        ans[strs[i]] = lst

                j += 1

        for k in visited:
            if k in ans:
                del ans[k]

        for v in ans.values():
            res.append(v)

        return res
