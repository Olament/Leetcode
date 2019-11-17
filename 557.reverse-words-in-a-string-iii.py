#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def split(self, s: str):
        lst = []
        pos = 0
        while pos < len(s):
            curr = ""
            #skip the whitespace
            while pos < len(s) and s[pos] == " ":
                pos += 1
            while pos < len(s) and s[pos] != " ":
                curr += s[pos]
                pos += 1
            lst.append(curr)
        return lst
    def reverseWords(self, s: str) -> str:
        lst = self.split(s)
        for i in range(len(lst)):
            lst[i] = lst[i][::-1]
        return " ".join(lst)
        
# @lc code=end

