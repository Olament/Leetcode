#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False

        row, col = len(matrix), len(matrix[0])

        def topoint(num: int) -> (int, int):
            rp = num // col
            cp = num % col
            return (rp, cp)
        
        lb, rb = 0, (row*col) - 1
        while (lb <= rb):
            mid = lb + (rb-lb) // 2
            currR, currC = topoint(mid)
            if matrix[currR][currC] == target:
                return True
            elif matrix[currR][currC] > target:
                rb = mid-1
            else:
                lb = mid+1
        return False
# @lc code=end

