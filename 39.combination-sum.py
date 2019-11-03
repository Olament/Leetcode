#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        lst = []
        candidates.sort()

        def search(index, sum, comb):
            if sum > target:
                return
            if sum == target:
                lst.append(comb)
                return
            
            for i in range(index, len(candidates)):
                search(i, sum+candidates[i], comb+[candidates[i]])

        search(0, 0, [])
        return lst
# @lc code=end

