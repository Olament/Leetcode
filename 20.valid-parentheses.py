#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (35.67%)
# Likes:    3478
# Dislikes: 169
# Total Accepted:    728.4K
# Total Submissions: 1.9M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

# @lc code=start
import queue

class Solution:
    def isLeft(self, c: chr) -> bool:
        if c == '(' or c == '{' or c == '[':
            return True
        return False
    
    def isMatch(self, l: chr, r: chr) -> bool:
        if (l == '(' and r == ')') or (l == '{' and r == '}') or (l == '[' and r == ']'):
           return True
        return False

    def isValid(self, s: str) -> bool:
        q = []
        for c in s:
            if self.isLeft(c):
                q.append(c)
            elif len(q) == 0 or not self.isMatch(q.pop(), c):
                return False
        if len(q) == 0:
            return True
        return False
# @lc code=end

