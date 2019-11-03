#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        def checkVowels(c: chr) -> bool:
            return c.lower() in ['a', 'e', 'i', 'o', 'u']
        
        lst = []
        for c in s:
            if checkVowels(c):
                lst.insert(0, c)
        
        string: str = ""
        for c in s:
            if checkVowels(c):
                string += lst[0]
                lst = lst[1:]
            else:
                string += c
        
        return string
# @lc code=end

