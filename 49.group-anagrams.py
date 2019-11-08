#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sortedString = ""
            for ch in sorted(s):
                sortedString += ch
            if sortedString not in anagrams:
                anagrams[sortedString] = [s]
            else:
                anagrams[sortedString].append(s)

        return list(anagrams.values())
            


# @lc code=end

