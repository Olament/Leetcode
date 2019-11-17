#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        def printMatrix(mat):
            for row in mat:
                print(row)

        printMatrix(matrix)
        print(" ")
        m = len(matrix)
        n = len(matrix[0])
        for i in range(len(matrix)//2 + 1):
            for j in range(len(matrix[0])//2 + 1):
                matrix[i][j], matrix[i][n-j-1], matrix[m-i-1][n-j-1], matrix[m-i-1][j] = \
                    matrix[m-i-1][j], matrix[i][j], matrix[i][n-j-1], matrix[m-i-1][n-j-1]
        printMatrix(matrix)

        
# @lc code=end

