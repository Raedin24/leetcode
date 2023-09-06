#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(None, head)
        curr_node = node_head = head
        index = 0
        while curr_node:
            curr_node = curr_node.next
            index += 1
        curr_node = head
        for i in range(1, index - n):
            curr_node = curr_node.next
        if index - n == 0:
            dummy_node.next = dummy_node.next.next
            return dummy_node.next
        curr_node.next = curr_node.next.next
        return dummy_node.next   
# @lc code=end

