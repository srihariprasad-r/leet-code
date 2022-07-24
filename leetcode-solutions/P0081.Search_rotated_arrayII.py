class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        if len(nums) == 1 and nums[-1] == target:
            return True

        # left = 0
        # right = len(nums) - 1

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end)/2

            if nums[mid] == target:
                return True

            if nums[start] < nums[mid]:
                if target < nums[start] or target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[start] > nums[mid]:
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                start += 1

        return False