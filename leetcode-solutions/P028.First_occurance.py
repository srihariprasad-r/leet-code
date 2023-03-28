class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

# KMP
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        arr = [0] * len(needle)
        i = 1
        j = 0

        while i < len(needle):
            if needle[i] == needle[j]:
                arr[i] = j + 1
                j += 1
                i += 1
            elif j == 0:
                arr[i] = 0
                i += 1
            else:
                j = arr[j-1]

        i = 0
        j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = arr[j-1]

            if j == len(needle):
                return i - len(needle)

        return -1
