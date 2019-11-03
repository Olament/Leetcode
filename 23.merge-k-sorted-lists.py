#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lst = ListNode(0)
        p = lst

        while True:
            val = float('inf')
            index = -1

            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val < val:
                        val = lists[i].val
                        index = i
            
            if index == -1:
                break
            else:
                p.next = ListNode(val)
                lists[index] = lists[index].next
                p = p.next
        
        return lst.next

        
# @lc code=end

