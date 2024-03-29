#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (39.95%)
# Likes:    2695
# Dislikes: 341
# Total Accepted:    463.1K
# Total Submissions: 1.1M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# Example:
# 
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#

# @lc code=start
class Solution:
    dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
    
    def product(self, lst: [str], c: chr) -> [str]:
        if len(lst) == 0:
            return self.dic[c]
        
        alph = self.dic[c]
        newList = []
        for i in range(len(lst)):
            for j in range(len(alph)):
                newList.append(lst[i]+alph[j])
        
        return newList

    def letterCombinations(self, digits: str) -> [str]:
        lst = []
        for c in digits:
            lst = self.product(lst, c)
        
        return lst

        
# @lc code=end

