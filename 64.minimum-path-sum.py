#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        lst = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]

        lst[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and j > 0:
                    lst[i][j] = min(grid[i][j]+lst[i-1][j], grid[i][j]+lst[i][j-1])
                if i == 0 and j > 0:
                    lst[i][j] = grid[i][j] + lst[i][j-1]
                if i > 0 and j == 0:
                    lst[i][j] = grid[i][j] + lst[i-1][j]
        
        return lst[len(grid)-1][len(grid[0])-1]
# @lc code=end

