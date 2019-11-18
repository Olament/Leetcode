#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        
        return sum - len(nums) * (len(nums) - 1) // 2
        
# @lc code=end

