#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        lst = []
        candidates.sort()

        def search(index, currlst, sum):
            if sum == target:
                lst.append(currlst)
                return
            if sum > target:
                return
            
            for i in range(index, len(candidates)):
                if (i > index and candidates[i] == candidates[i-1]):
                    continue
                search(i+1, currlst+[candidates[i]], sum+candidates[i])
        search(0, [], 0)

        return lst
# @lc code=end

