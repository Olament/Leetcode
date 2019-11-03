#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = [(1000, 'M'),
               (900, 'CM'),
               (500, 'D'),
               (400, 'CD'),
               (100, 'C'),
               (90, 'XC'),
               (50, 'L'),
               (40, 'XL'),
               (10, 'X'),
               (9, 'IX'),
               (5, 'V'),
               (4, 'IV'),
               (1, 'I')]
    
        rom = ''
        while num > 0:
            for val, dig in dic:
                if num >= val:
                    num -= val
                    rom += dig
                    break
        return rom
        
# @lc code=end

