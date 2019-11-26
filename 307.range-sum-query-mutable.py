#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = [0 for i in range(len(nums)+1)]
        self.nums = nums
        rollingSum = 0

        for i in range(len(nums)):
            self.sum[i+1] = nums[i] + rollingSum
            rollingSum += nums[i]
        
    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        for k in range(i+1, len(self.sum)):
            self.sum[k] += diff

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j+1] - self.sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end

