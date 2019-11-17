#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def isSign(self, ch):
        return ch == '*' or ch == '+' or ch == '-' or ch == '/'
    
    def findIndex(self, sign):
        for i in range(len(sign)):
            if sign[i] == '*' or sign[i] == '/':
                return i
        return 0

    def calculate(self, s: str) -> int:
        number = []
        sign = []

        pos = 0
        while pos < len(s):
            if s[pos] == ' ':
                pos += 1
            elif self.isSign(s[pos]):
                sign.append(s[pos])
                pos += 1
            else:
                end = pos
                while end < len(s)-1 and s[end+1].isdigit():
                    end += 1
                number.append(int(s[pos:end+1]))
                pos = end + 1
        
        while len(number) > 1:
            index = self.findIndex(sign)
            
            res = 0
            if sign[index] == '+':
                res = number[index] + number[index+1]
            elif sign[index] == '-':
                res = number[index] - number[index+1]
            elif sign[index] == '*':
                res = number[index] * number[index+1]
            else:
                res = number[index] // number[index+1]
            
            number[index] = res
            number.pop(index+1)
            sign.pop(index)
        
        return number[0]
# @lc code=end

