#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lst = []

        def search(index, subset):
            lst.append(subset)
            for i in range(index, len(nums)):
                if len(subset) == 0 or nums[i] != subset[-1]:
                    search(i+1, subset+[nums[i]])
        
        search(0, [])

        return lst
# @lc code=end

