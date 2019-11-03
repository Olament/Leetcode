#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        curr = 1
        while curr < n:
            curr *= 3
        
        return curr == n
        
# @lc code=end

