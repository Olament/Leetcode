#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1p = l1
        l2p = l2

        node = ListNode(0)
        nodep = node
        
        res = False

        while l1p or l2p:
            num1 = num2 = 0
            if l1p:
                num1 = l1p.val
                l1p = l1p.next
            if l2p:
                num2 = l2p.val
                l2p = l2p.next

            currsum = num1+num2+(1 if res else 0)
            res = False
            if currsum > 9:
                res = True
                currsum = currsum - 10
            
            nodep.next = ListNode(currsum)
            nodep = nodep.next

        if res:
            nodep.next = ListNode(1)

        return node.next 
# @lc code=end

