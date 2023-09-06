#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        curr_node = head
        original = ListNode(None)
        orig_head = original
        while curr_node:
            if original.val == None:
                original.val = curr_node.val
                curr_node = curr_node.next
                continue
            new_node = ListNode(curr_node.val)
            original.next = new_node
            curr_node = curr_node.next
            original = original.next
        curr_node = head
        while curr_node:
            next = curr_node.next
            curr_node.next = prev
            prev = curr_node
            if next == None:
                break
            curr_node = next
        self.head = curr_node
        while orig_head and curr_node:
            if curr_node.val != orig_head.val:
                return False
            curr_node = curr_node.next
            orig_head = orig_head.next
        return True     
# @lc code=end