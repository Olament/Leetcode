#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0:
            return ''
        if n == 1:
            return "1"

        seq = "1"
        for _ in range(1, n):
            prev, count = seq[0], 0
            newSeq = ""
            for ch in seq:
                if ch != prev:
                    newSeq += str(count)+prev
                    prev, count = ch, 1
                else:
                    count += 1
            newSeq += str(count)+prev
            seq = newSeq
        
        return seq
            

        
# @lc code=end

