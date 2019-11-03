#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        inputs = preorder.split(',')
        stack = []
        for input in inputs:
            stack.append(input)
            while stack[-2:] == ['#','#'] and len(stack)>2 and stack[-3]!='#':
                stack = stack[:-3]+['#']
        return stack == ['#']
# @lc code=end

