#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        numberOfZero = 0

        while fast < len(nums):
            while fast < len(nums) and nums[fast] == 0:
                fast += 1
                numberOfZero += 1
            
            if fast < len(nums) and fast > slow:
                nums[slow] = nums[fast]
            
            slow += 1
            fast += 1
        
        for i in range(numberOfZero):
            nums[-1-i] = 0
        
# @lc code=end

