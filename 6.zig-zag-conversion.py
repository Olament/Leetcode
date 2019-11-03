#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        lst = [''] * numRows
        index, step = 0, 1

        for x in s:
            lst[index] += x
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        
        return ''.join(lst)
# @lc code=end

