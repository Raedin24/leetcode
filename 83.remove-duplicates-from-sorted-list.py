#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        next_node = head
        while curr_node:

            while curr_node.val == next_node.val:
                next_node = next_node.next
                if next_node == None:
                    break
            curr_node.next = next_node
            curr_node = curr_node.next
        return head       
# @lc code=end

