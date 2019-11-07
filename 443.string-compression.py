#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = 0
        while curr < len(chars):
            number = 1
            while curr+1 < len(chars) and chars[curr] == chars[curr+1]:
                number += 1
                chars.pop(curr+1)
            
            if number == 1:
                curr = curr+1
            else:
                chars = chars[:curr+1] + [str(number)] + chars[curr+1:]
                curr = curr+2
        
        print(chars)
# @lc code=end

