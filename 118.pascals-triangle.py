#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1], [1, 1]]
        if numRows <= 2:
            return lst[:numRows]
        
        for i in range(2, numRows):
            currRow = []
            for j in range(1, i):
                currRow.append(lst[i-1][j]+lst[i-1][j-1])
            lst.append([1]+currRow+[1])
        
        return lst      
# @lc code=end

