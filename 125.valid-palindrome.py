#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for ch in s.lower():
            if ch.isalnum():
                newStr += ch

        if len(newStr) % 2 == 0:
            return self.search(len(newStr) // 2 - 1, len(newStr) // 2, newStr)

        return self.search(len(newStr)//2, len(newStr)//2, newStr)
    
    def search(self, lp, rp, word):
        if lp < 0 or rp >= len(word):
            return True
        
        if word[lp] != word[rp]:
            return False
        
        return self.search(lp-1, rp+1, word)
        
# @lc code=end

