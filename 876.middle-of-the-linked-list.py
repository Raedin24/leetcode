#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        curr_node = head
        while curr_node:
            curr_node = curr_node.next
            index += 1
        curr_node = head
        for i in range((index//2)):
            curr_node = curr_node.next
        return curr_node       
# @lc code=end

