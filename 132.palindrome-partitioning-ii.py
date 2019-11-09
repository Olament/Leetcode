#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str):
            return s == s[::-1]

    def minCut(self, s: str) -> int:
        res = []
        def search(currStr, currPar):
            if len(currStr) == 0:
                res.append(currPar)
            
            for i in range(1, len(currStr)+1):
                if self.isPalindrome(currStr[:i]):
                    search(currStr[i:], currPar+[currStr[:i]])
    
        search(s, [])

        minC = len(res[0]) - 1
        for i in range(1, len(res)):
            if len(res[i])-1 < minC:
                minC = len(res[i]) - 1
        
        return minC
# @lc code=end

