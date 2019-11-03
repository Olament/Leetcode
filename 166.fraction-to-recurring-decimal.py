#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        lst = []

        while numerator != 0:
            num = str(numerator // denominator)
            if len(lst) >= 2 and num == lst[-1]:
                lst[-1] = "("+lst[-1]+")"
                break
            lst.append(num)
            numerator = (numerator % denominator) * 10
        
        if len(lst) == 1:
            return ''.join(lst)
        else:
            return lst[0]+'.'+''.join(lst[1:])
        
s = Solution()
print(s.fractionToDecimal(4, 333))
# @lc code=end

