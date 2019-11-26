#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sumMatrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                top, left, topleft = 0, 0, 0
                if i > 0:
                    top = self.sumMatrix[i-1][j]
                if j > 0:
                    left = self.sumMatrix[i][j-1]
                if i > 0 and j > 0:
                    topleft = self.sumMatrix[i-1][j-1]
                
                self.sumMatrix[i][j] = matrix[i][j] + top + left - topleft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top, left, topleft = 0, 0, 0
        if col1 > 0:
            left = self.sumMatrix[row2][col1-1]
        if row1 > 0:
            top = self.sumMatrix[row1-1][col2]
        if col1 > 0 and row1 > 0:
            topleft = self.sumMatrix[row1-1][col1-1]

        return self.sumMatrix[row2][col2] - top - left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

