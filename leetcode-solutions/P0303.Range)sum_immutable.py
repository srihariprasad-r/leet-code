class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = []
        n = len(nums)
        s = 0
        for i, num in enumerate(nums):
            s += num
            self.prefix.append(s)

    def sumRange(self, left: int, right: int) -> int:
        r = self.prefix[right]
        l = self.prefix[left-1] if left > 0 else 0

        return r - l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
