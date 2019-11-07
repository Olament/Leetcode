#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(node):
            prev = None
            nextp = None
            while node:
                nextp = node.next
                node.next = prev
                prev = node
                node = nextp
            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)

        dummy = ListNode(0)

        def addList(lst1, lst2, newList, carry):
            if not lst1 and not lst2:
                if carry:
                    newList.next = ListNode(1)
                return
            
            val1, newLst1 = 0, None
            val2, newLst2 = 0, None

            if lst1:
                val1 = lst1.val
                newLst1 = lst1.next
            if lst2:
                val2 = lst2.val
                newLst2 = lst2.next
            
            
            newSum = val1 + val2
            if carry:
                newSum += 1
            newList.next = ListNode(newSum % 10)
            newList = newList.next

            if newSum > 9:
                addList(newLst1, newLst2, newList, True)
            else:
                addList(newLst1, newLst2, newList, False)
        
        p = dummy
        addList(l1, l2, p, False)
        
        return reverse(dummy.next) 
# @lc code=end

