class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new_list = zip(nums[:n], nums[n:])
        del nums[:]
        for i in range(len(new_list)):
            nums.append(new_list[i][0])
            nums.append(new_list[i][1])
        
        return nums