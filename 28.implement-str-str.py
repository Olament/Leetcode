#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            matched = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    matched = False
                    break
            if matched:
                return i
        return -1
# @lc code=end

