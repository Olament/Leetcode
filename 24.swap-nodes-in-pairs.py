#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        fast = head.next
        slow = head

        while fast:
            temp = fast.val
            fast.val = slow.val
            slow.val = temp

            fast = fast.next.next if fast.next and fast.next.next else None
            slow = slow.next.next if slow.next and slow.next.next else None
        
        return head

        
# @lc code=end

