#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    isValid = False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set()
        for word in wordDict:
            dic.add(word)
        
        canBreak = [False] * (len(s) + 1)
        canBreak[0] = True

        for i in range(len(s)):
            for j in range(i, len(s)):
                if canBreak[i] and s[i:j+1] in dic:
                    canBreak[j+1] = True
        
        return canBreak[-1]
# @lc code=end

