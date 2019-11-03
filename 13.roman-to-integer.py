#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'M': 1000,
               'D': 500,
               'C': 100,
               'L': 50,
               'X': 10,
               'V': 5,
               'I': 1}
            
        prevCh = None
        sumr = 0
        for ch in s:
            sumr += dic[ch]
            if prevCh and dic[prevCh] < dic[ch]:
                sumr -= dic[prevCh] * 2
            prevCh = ch
        
        return sumr
            

        

# @lc code=end

