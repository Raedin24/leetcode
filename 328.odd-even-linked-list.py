#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node1, dummy_node2 = ListNode(None), ListNode(None)
        dummy1, dummy2 = dummy_node1, dummy_node2
        curr_node = head

        while curr_node:

            dummy1.next = curr_node
            dummy2.next = curr_node.next
            prev = dummy1
            dummy1, dummy2 = dummy1.next, dummy2.next
            if not curr_node.next:
                break
            curr_node = curr_node.next.next

        if dummy1:
            dummy1.next = dummy_node2.next
        else:
            prev.next = dummy_node2.next

        return dummy_node1.next       
# @lc code=end

