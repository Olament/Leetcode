#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        currProduct = 1
        lst = []
        for i in range(len(nums)):
            lst.append(currProduct)
            currProduct = currProduct * nums[i]
        
        currProduct = 1
        for i in range(len(nums)-1, -1, -1):
            lst[i] *= currProduct
            currProduct *= nums[i]
        
        return lst

# @lc code=end

