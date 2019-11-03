#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

        while slow:
            while fast.next and slow.next.val == fast.next.val:
                fast = fast.next
            if slow.next != fast:
                slow.next = fast.next
                fast = slow
            else:
                slow = fast        
        return dummy.next
# @lc code=end

