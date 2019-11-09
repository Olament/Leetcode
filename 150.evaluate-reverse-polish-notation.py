#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if token == '+':
                    stack.append(val1+val2)
                elif token == '-':
                    stack.append(val2 - val1)
                elif token == '*':
                    stack.append(val1*val2)
                elif token == '/':
                    stack.append(int(val2 / float(val1)))
            else:
                stack.append(int(token))
        return stack.pop()
            
        
        
# @lc code=end

