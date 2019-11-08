#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def search(step, currIP, currS):
            if step == 4:
                if len(currS) == 0:
                    res.append('.'.join(currIP))
                return
            
            if (4 - step) * 3 < len(currS):
                return
            
            for i in range(min(len(currS), 3)):
                if 0 <= int(currS[:i+1]) <= 255 and not(len(currS[:i+1]) > 1 and currS[:i+1][0] == '0'):
                    search(step+1, currIP+[currS[:i+1]], currS[i+1:])
        search(0, [], s)
        return res
# @lc code=end

