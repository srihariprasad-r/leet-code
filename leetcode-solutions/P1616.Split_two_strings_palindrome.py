class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        n = len(a)
        i = j = 0

        while i <= n//2 and a[i] == b[n-i-1]:
            i += 1

        while j <= n//2 and b[j] == a[n-j-1]:
            j += 1

        left = max(i, j)
        right = n - 1 - left

        while right - left >= 1 and a[left] == a[right]:
            left += 1
            right -= 1

        if right - left < 1:
            return True

        left = max(i, j)
        right = n - 1 - left

        while right - left >= 1 and b[left] == b[right]:
            left += 1
            right -= 1

        if right - left < 1:
            return True

        return False
