#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        lb, rb = 0, len(nums)-1
        maxP = nums[0]
        product = 1
        for num in nums:
            product *= num
        while lb <= rb:
            maxP = max(maxP, product)

            leftProduct = 1
            rightProduct = 1
            for i in range(lb, rb):
                leftProduct *= nums[i]
            for i in range(lb+1, rb+1):
                rightProduct *= nums[i]
            
            product = max(leftProduct, rightProduct)
            if leftProduct < rightProduct:
                lb += 1
            else:
                rb -= 1 
        return maxP

# @lc code=end

