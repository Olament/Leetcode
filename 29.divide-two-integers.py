#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = not ((dividend >= 0) == (divisor >= 0))
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while dividend >= divisor:
            dividend -= divisor
            result += 1
        print(sign)
        return -result if sign else result
# @lc code=end

