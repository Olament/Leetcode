#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(lst, i, j):
            if i == j:
                return
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

        rp, wp, bp = 0, 0, len(nums)-1
        while wp <= bp:
            if nums[wp] == 0:
                swap(nums, wp, rp)
                wp += 1
                rp += 1
            elif nums[wp] == 1:
                wp += 1
            else:
                swap(nums, bp, wp)
                bp -= 1
# @lc code=end

