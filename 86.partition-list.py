#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        curr_node = head

        dummy1 = dummy_node1 = ListNode(None)
        dummy2 = dummy_node2 = ListNode(None)
        while curr_node:
            if curr_node.val < x and dummy_node1.val == None:
                dummy_node1 = curr_node
                dummy1 = dummy_node1
            elif curr_node.val < x:
                dummy_node1.next = curr_node
                dummy_node1 = dummy_node1.next
            if curr_node.val >= x and dummy_node2.val == None:
                dummy_node2 = curr_node
                dummy2 = dummy_node2
            elif curr_node.val >= x:
                dummy_node2.next = curr_node
                dummy_node2 = dummy_node2.next
            curr_node = curr_node.next
        dummy_node2.next = None
        if dummy1.val is not None and dummy2.val is not None:
            dummy_node1.next = dummy2
        elif dummy2.val is None:
            return dummy1
        else:
            return dummy2
        return dummy1
    
# @lc code=end

