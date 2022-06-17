class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if (target < letters[0]) or (letters[-1] <= target):
            return letters[0]

        left = 0
        right = len(letters) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid
            else:
                right = mid

        return letters[right]
