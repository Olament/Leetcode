#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p and not s:
            return True
        if not p or not s:
            return False
        
        pindex = 0
        for x in s:
            if pindex >= len(p):
                return False
            if p[pindex] == '*':
                pindex -= 1
            
            if p[pindex] != x and p[pindex] != '.':
                return False
            pindex += 1
        
        return True

# @lc code=end

