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

        slow, fast = dummy, dummy.next.next

        while fast:
            while fast and fast.val == slow.next.val:
                fast = fast.next
            slow.next.next = fast
            slow = slow.next

        return dummy.next
# @lc code=end

