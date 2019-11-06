#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lb, rb = 0, len(nums)-1

        while lb < rb:
            mid = lb + (rb - lb) // 2
            if nums[mid] > nums[rb]:
                lb = mid + 1
            else:
                rb = mid
        return nums[lb]
# @lc code=end