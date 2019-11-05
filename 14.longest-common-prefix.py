#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs = sorted(strs, key=len)

        if len(strs) == 0:
            return prefix

        for ch in strs[0]:
            for i in range(len(strs)):
                if ch == strs[i][0]:
                    strs[i] = strs[i][1:]
                else:
                    return prefix
            prefix += ch
        
        return prefix
# @lc code=end

