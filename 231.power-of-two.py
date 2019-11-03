#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        if n % 2 != 0:
            return False
        
        num = 2
        while num < n:
            num *= 2
        
        if num == n:
            return True
        return False
# @lc code=end

