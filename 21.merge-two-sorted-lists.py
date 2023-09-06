#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        second = list2
        new_list = ListNode(None)
        new_head = new_list

        if not first:
            return second
        elif not second:
            return first
        while first:
            if first.val <= second.val:
                new_list.next = ListNode(first.val)
                new_list = new_list.next
                first = first.next
            else:
                new_list.next = ListNode(second.val)
                new_list = new_list.next
                second = second.next
            if first == None:
                new_list.next = second
                break
            elif second == None:
                new_list.next = first
                break
        return new_head.next
# @lc code=end