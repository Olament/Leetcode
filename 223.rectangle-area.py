#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        rec1 = rec2 = [0] * 4
        if A > E:
            rec1 = [A, B, C, D]
            rec2 = [E, F, G, H]
        else:
            rec2 = [A, B, C, D]
            rec1 = [E, F, G, H]
        
        def calArea(x1, y1, x2, y2):
            return abs(x2-x1) * abs(y2-y1)
        
        overlap = 0
        if not (rec1[1] >= rec2[3] or rec2[1] >= rec1[3]):
            if rec1[1] < rec2[3]:
                overlap = calArea(rec1[2], rec1[1], rec2[0], rec2[3])
            else:
                overlap = calArea(rec2[2], rec2[1], rec1[0], rec1[3])
        
        return calArea(rec1[0], rec1[1], rec1[2], rec1[3]) * calArea(rec2[0], rec2[1], rec2[2], rec2[3]) - overlap

        
# @lc code=end

