#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        
        lb = 0
        rb = len(nums) - 1

        while lb < rb:
            mid = lb + (rb - lb) // 2
            if nums[mid] > nums[mid+1]:
                rb = mid
            else:
                lb = mid + 1
        
        return lb


# @lc code=end

