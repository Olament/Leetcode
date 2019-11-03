#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if (i == 0 or nums[i-1] < target) and nums[i] > target:
                return i
        return len(nums)
# @lc code=end

