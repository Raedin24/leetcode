#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr_node = head
        while curr_node:
            curr_node = curr_node.next
            if curr_node.next == None:
                dummy.next = head
                head = curr_node  
# @lc code=end


