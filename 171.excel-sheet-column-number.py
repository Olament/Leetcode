#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        lst = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = 0

        for i, val in enumerate(s[::-1]):
            num += (lst.index(val)+1) * (26**i)
        
        return num
# @lc code=end

