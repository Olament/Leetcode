#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def toIndex(self, s: str):
        indexString = ""
        lst = []
        for ch in s:
            if ch not in lst:
                lst.append(ch)
            else:
                index = lst.index(ch)
                indexString += str(index) if index > 9 else "0"+str(index)
        return indexString

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.toIndex(s) == self.toIndex(t)
        
# @lc code=end

