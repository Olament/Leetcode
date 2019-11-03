#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        lst = []
        tmp = []
        for i in nums:
            if len(tmp) == 0:
                tmp.append(i)
            else:
                if (i - 1) == tmp[-1]:
                    tmp.append(i)
                else:
                    lst.append(tmp)
                    tmp = []
                    tmp.append(i)
            
            print(tmp)
            print(lst)
        
        if len(tmp) != 0:
            lst.append(tmp)

        output = []
        for i in lst:
            if len(i) == 1:
                output.append(str(i[0]))
            else:
                output.append(str(i[0])+"->"+str(i[-1]))

        return output

        
# @lc code=end

