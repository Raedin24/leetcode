#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(None, head)

        before = dummy_node
        curr_node = head
        for l in range(left-1):
            before = curr_node
            curr_node = curr_node.next

        prev = None
        for i in range(right-left+1):
            next = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next
        before.next.next = curr_node
        before.next = prev

        head = dummy_node.next
        return head
# @lc code=end