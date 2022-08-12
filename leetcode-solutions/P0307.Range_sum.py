"""
Notes:
i + (i & - i)
1.get 1's complement ( invert 1/0 expect first bit)
2. add 1 to 1's complement
3. with #2, AND with same number(i) => i & - i
4. with #3, add(+) with same nmber

0101 -> input
0010 -> 1's complement
+1
----
0011

-> i & - i 
0011  & 
0101
-----
0001 
-----

-> i + (i & - i)

0001 + 
0101
-----
0110
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        
        for i, num in enumerate(nums):
            self.treeupdate(i+1, num)
            
    def treeupdate(self, idx, val):
        while idx <= len(self.nums):
            self.tree[idx] += val
            idx += idx&-idx # finds next node to update

    def range(self, idx):
        ans = 0
        while idx > 0:
            ans += self.tree[idx]
            idx -= idx&-idx # finds parent
            
        return ans
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        diff = val - self.nums[index]
        self.nums[index] = val
        self.treeupdate(index+1, diff)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.range(right+1) - self.range(left+1-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)