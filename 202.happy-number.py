#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        sets = set()

        while n != 1:
            sums = 0
            sets.add(n)
            while n > 0:
                sums += (n % 10) ** 2
                n = n // 10
            if sums in sets:
                return False
            n = sums
        
        return True
        
# @lc code=end

