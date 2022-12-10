# TLE

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []

        def palindrome(w, s, e):
            while s <= e:
                if w[s] != w[e]:
                    return False
                else:
                    s += 1
                    e -= 1

            return True

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if palindrome(words[i] + words[j], 0, len(words[i] + words[j]) - 1):
                        ans.append([i, j])

        return ans
