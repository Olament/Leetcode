#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lst = [[0 for x in range(n)] for y in range(m)]

        lst[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    lst[i][j] += lst[i-1][j]
                if j > 0:
                    lst[i][j] += lst[i][j-1]
        print(lst)
        return lst[m-1][n-1]
# @lc code=end

