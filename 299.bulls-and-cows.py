#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        dic = {}
        unmatched = []

        # dic for appearance
        for i in range(len(secret)):
            if secret[i] not in dic:
                dic[secret[i]] = set()
            dic[secret[i]].add(i)
        
        # search for bulls
        for i in range(len(guess)):
            if guess[i] in dic:
                if i in dic[guess[i]]:
                    bulls += 1
                    dic[guess[i]].remove(i)
                else:
                    unmatched.append(guess[i])
        for ch in unmatched:
            if ch in dic and len(dic[ch]) > 0:
                cows += 1
                dic[ch].pop()
        
        return str(bulls) + 'A' + str(cows) + 'B'

# @lc code=end
