class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        lng = 0

        for n in nums:
            if (n -1) not in s:
                length = 0
                while n + length in s:
                    length += 1
                lng = max(lng, length)

        return lng