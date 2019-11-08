#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst = []
        def combine(comb, aval):
            if len(comb) + len(aval) < k:
                return
            if len(comb) == k:
                lst.append(comb)
                return
            
            for i in range(len(aval)):
                combine(comb+[aval[i]], aval[i+1:])
        
        combine([], [i for i in range(1, (n+1))])
        return lst
# @lc code=end

