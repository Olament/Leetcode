#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lst = []
        def search(curr):
            if len(curr) == len(nums):
                lst.append(curr)
                return

            for i in range(len(nums)):
                if nums[i] not in curr:
                    search(curr+[nums[i]])      
        
        search([])

        return lst

# @lc code=end

