#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build dictionary
        dic = {}
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if j == i:
                    continue 
                if self.oneChAway(wordList[i], wordList[j]):
                    if wordList[i] in dic:
                        dic[wordList[i]].append(wordList[j])
                    else:
                        dic[wordList[i]] = [wordList[j]]
        
        dic[beginWord] = []
        for i in range(len(wordList)):
            if self.oneChAway(beginWord, wordList[i]):
                    dic[beginWord].append(wordList[i])

        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            currWord, currDepth = queue.pop(0)
            visited.add(currWord)
            if currWord == endWord:
                return currDepth
            
            for nextWord in dic[currWord]:
                if nextWord not in visited:
                    queue.append((nextWord, currDepth+1))
        
        return 0

    def oneChAway(self, str1, str2):
        diff = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
        return diff == 1
        
# @lc code=end

