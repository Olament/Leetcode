#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area = (C-A) * (D-B) + (G-E)*(H-F)
        
        # calculate overlap
        if (E > C) or (B > H) or (A > G) or (F > D):
            return area
        return area - (min(C, G) - max(A, E)) * (min(D, H)- max(B, F))
        
# @lc code=end

