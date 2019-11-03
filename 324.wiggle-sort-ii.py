#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst = sorted(nums, reverse=True)
        print(lst)

        last = 0
        if len(nums) % 2 != 0:
            last = lst[0]
            lst = lst[1:]
        
        mid = len(nums) // 2
        for i in range(mid):
            nums[2*i] = lst[mid+i]
            nums[2*i + 1] = lst[i]
        
        if len(nums) % 2 != 0:
            nums[-1] = last


        
        
# @lc code=end

