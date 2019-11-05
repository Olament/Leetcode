#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i, d1 in enumerate(num1[::-1]):
            temp = int(d1) * (10**i)
            for j, d2 in enumerate(num2[::-1]):
                res += temp * (int(d2) * (10**j))
        return str(res)

        
# @lc code=end

