#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None, head)
        prev = dummy_head
        curr_node = head
        while curr_node and curr_node.next:
            if curr_node.val != curr_node.next.val:
                prev = curr_node
                curr_node = curr_node.next

            elif curr_node.val == curr_node.next.val:
                while curr_node.next and curr_node.val == curr_node.next.val:
                    curr_node = curr_node.next
                prev.next = curr_node.next
                curr_node = curr_node.next

        return dummy_head.next     
# @lc code=end

