#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        res = [[0 if matrix[i][j] == '0' else 1 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        for i in range(1, len(res)):
            for j in range(1, len(res[0])):
                if res[i][j] == 1:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j], res[i][j-1]) + 1
                else:
                    res[i][j] = 0
        
        return length ** 2

# @lc code=end

