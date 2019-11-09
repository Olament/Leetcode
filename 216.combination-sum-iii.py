#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def search(currComb, currentSum, index):
            if len(currComb) == k:
                if currentSum == n:
                    res.append(currComb)
                return
            
            for i in range(index, 10):
                if currentSum + i <= n:
                    search(currComb+[i], currentSum+i, i+1)
        
        search([], 0, 1)
        return res
        
# @lc code=end

