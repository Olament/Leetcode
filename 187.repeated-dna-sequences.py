#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        dic = {}
        for i in range(0, len(s)-9):
            if s[i:i+10] in dic:
                dic[s[i:i+10]] += 1
            else:
                dic[s[i:i+10]] = 1
        
        lst = []
        for key, value in dic.items():
            if value > 1:
                lst.append(key)
        
        return lst
# @lc code=end

