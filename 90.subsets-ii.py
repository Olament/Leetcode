#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lst = []
        def search(num, currSet, aval):
            if num == 0:
                lst.append(currSet)
                return
            for i in range(len(aval)):
                search(num-1, currSet+[aval[i]], aval[:i]+aval[i+1:])
        
        for i in range(len(nums)+1):
            search(i, [], nums)
        
        return lst

# @lc code=end

