#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        lst = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
        div = 26
        res = []

        while n > 0:
            index = (n-1) % div
            n = (n-1) // div
            res.append(lst[index])
        res.reverse()
        return ''.join(res)


        
# @lc code=end

