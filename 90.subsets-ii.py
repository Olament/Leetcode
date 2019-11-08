#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lst = []
        nums.sort()
        def search(index, subset):
            if subset not in lst:
                lst.append(subset)
            
            for i in range(index, len(nums)):
                search(i+1, subset[:]+[nums[i]])
        
        search(0, [])
        return lst

# @lc code=end

