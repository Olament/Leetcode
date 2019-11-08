#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 1:
            return [1 for i in range(rowIndex+1)]
        
        prev = [1, 1]
        for i in range(2, rowIndex+1):
            currRow = []
            for j in range(1, i):
                currRow.append(prev[j-1]+prev[j])
            prev = [1]+currRow+[1]
        
        return prev
        
# @lc code=end

