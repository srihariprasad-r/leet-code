# wrong submission

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        c = ''
        st = set()

        def palindrome(s):
            k = 0
            m = 2
            while k < m:
                if s[k] != s[m]:
                    return False

                k += 1
                m -= 1

            return True

        for i in range(len(s)-2):
            j = i + 1
            k = i + 2
            while j < k and k < len(s):
                c = s[i]
                c += s[j]
                c += s[k]

                if palindrome(c):
                    st.add(c)
                    j += 1
                else:
                    k += 1

        return len(st)
