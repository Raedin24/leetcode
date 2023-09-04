#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None   

    def get(self, index: int) -> int:
        start_index = 0
        curr_node = self.head
        while curr_node:
            if start_index == index:
                return curr_node.value
            start_index += 1
            curr_node = curr_node.next
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = node(val)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        new_node = node(val)
        curr_node = self.head
        start_index = 0
        while curr_node: # 0 - 1
            if start_index == index - 1 or curr_node.next == None:
                new_node.next = curr_node.next
                curr_node.next = new_node # 1 - 3
                return
            curr_node = curr_node.next
            start_index += 1


    def deleteAtIndex(self, index: int) -> None:
        if index==0:
            if self.head:
                self.head = self.head.next
        curr_node = self.head
        start_index = 0
        while curr_node:
            if start_index==index-1 and curr_node.next:
                curr_node.next = curr_node.next.next
            curr_node=curr_node.next
            start_index+=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end