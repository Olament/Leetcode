#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = []
        def search(index, subset):
            lst.append(subset)
            for i in range(index, len(nums)):
                if (i > index and nums[i] == nums[i-1]):
                    continue
                search(i+1, subset+[nums[i]])
        
        search(0, [])

        return lst
# @lc code=end

