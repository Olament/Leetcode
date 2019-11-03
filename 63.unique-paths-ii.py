#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: 

        lst = [[0 for x in range(len(obstacleGrid[0]))] for y in range(len(obstacleGrid))]

        if obstacleGrid[0][0] != 1:
            lst[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                
                if i > 0:
                    lst[i][j] += lst[i-1][j]
                if j > 0:
                    lst[i][j] += lst[i][j-1]
        
        return lst[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
# @lc code=end

