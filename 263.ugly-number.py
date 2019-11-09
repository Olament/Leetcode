#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
            
        while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            else:
                num /= 5
        
        if num == 1:
            return True
        return False

        
# @lc code=end

