#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
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

        fast = slow = head

        while slow:
            while fast.next and fast.next.val == slow.val:
                fast = fast.next
            slow.next = fast.next
            slow = fast.next
            fast = fast.next
        
        return head
# @lc code=end

