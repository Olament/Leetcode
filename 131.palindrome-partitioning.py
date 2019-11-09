#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        res = []
        def search(currStr, currPar):
            if len(currStr) == 0:
                res.append(currPar)
            
            for i in range(1, len(currStr)+1):
                if self.isPalindrome(currStr[:i]):
                    search(currStr[i:], currPar+[currStr[:i]])
    
        search(s, [])

        return res 

        
# @lc code=end

