#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = 0
        end = -1
        for i in range(len(s)-1, -1, -1):
            if end == -1:
                if s[i] == ' ':
                    continue
                else:
                    end = i
            elif s[i] == ' ':
                start = i+1
                break
            
        if end == -1:
            return 0
        return end-start+1

        
# @lc code=end

