#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = [int(val) for val in version1.split('.')]
        lst2 = [int(val) for val in version2.split('.')]

        while lst1 and lst2:
            if lst1[0] > lst2[0]:
                return 1
            elif lst1[0] < lst2[0]:
                return -1
            lst1 = lst1[1:]
            lst2 = lst2[1:]
        
        if not lst1 and not lst2 or sum(lst1)+sum(lst2) == 0:
            return 0
        elif not lst2:
            return 1
        else:
            return -1
        
# @lc code=end

