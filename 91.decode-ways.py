#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        combination = [0 for i in range(len(s)+1)]

        combination[0] = 1
        combination[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s)+1):
            if s[i-1] != '0':
                combination[i] += combination[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                combination[i] += combination[i-2]

        return combination[len(s)]
        
# @lc code=end

