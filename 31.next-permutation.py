#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums: [int], i: int, j: int):
            temp: int = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        def smallest(nums: [int], pos: int, comp: int) -> int:
            value = 999999
            index = -1
            for i in range(pos, len(nums)):
                if nums[i] > nums[comp] and nums[i] < value:
                    value = nums[i]
                    index = i

            return index
        
        def find(pos: int):
            if pos > 0:
                if smallest(nums, pos, pos - 1) != -1:
                    swap(nums, smallest(nums, pos, pos - 1), pos - 1)
                else:
                    find(pos - 1)
            
            if smallest(nums, pos + 1, pos) != -1:
                swap(nums, smallest(nums, pos + 1, pos), pos)
        
        find(len(nums) - 1)
# @lc code=end

