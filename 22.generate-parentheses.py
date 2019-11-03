#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        def backtack(comb: str, numberOfLeft: int, numberOfRight: int):
            if numberOfLeft == 0 and numberOfRight == 0:
                output.append(comb)
                return
            
            if numberOfLeft > 0:
                backtack(comb+"(", numberOfLeft - 1, numberOfRight)
            if numberOfRight > numberOfLeft:
                backtack(comb+")", numberOfLeft, numberOfRight - 1)
        
        output = []
        backtack("", n, n)

        return output
# @lc code=end

