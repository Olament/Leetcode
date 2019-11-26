#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dic = {}
        str = str.split()
        
        if len(str) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if str[i] in dic.values():
                    return False
                dic[pattern[i]] = str[i]
            elif dic[pattern[i]] != str[i]:
                return False
        
        return True
# @lc code=end

