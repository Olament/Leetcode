#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perDic = {}
        for ch in s1:
            if ch not in perDic:
                perDic[ch] = 1
            else:
                perDic[ch] += 1

        for i in range(len(s2) - len(s1) + 1):
            currDic = {}
            for j in range(i, i+len(s1)):
                if s2[j] not in currDic:
                    currDic[s2[j]] = 1
                else:
                    currDic[s2[j]] += 1
            
            isSame = True
            for (key, value) in perDic.items():
                if key not in currDic or currDic[key] != value:
                    isSame = False
                    break 
            
            if isSame:
                return True
        
        return False 
                 

            
        
# @lc code=end

