#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums

        def permute(numbers):
            if len(numbers) == 1:
                return [numbers]
            
            lst = []
            for index, val in enumerate(numbers):
                if index > 0 and numbers[index-1] == val:
                    continue
                for p in permute(numbers[0:index]+numbers[index+1:]):
                    lst.append([val] + p)
            return lst
        
        return permute(sorted(nums))

        
# @lc code=end

