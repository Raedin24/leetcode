#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start
class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.init = k
        self.dummy = Node()
        self.tail = self.dummy.prev
        

    def enQueue(self, value: int) -> bool:
        self.value = value
        new_node = Node(self.value)
        dummy = self.dummy
        tail = self.tail
        if self.isFull() == True:
            return False
        elif dummy.next == None: 
            dummy.next = new_node
            new_node.next = dummy
            dummy.prev = new_node
            new_node.prev = dummy
            self.tail = new_node
        else:
            tail.next = new_node
            tail.next.prev = tail
            tail = tail.next
            tail.next = dummy
            dummy.prev = tail
            self.tail = tail
        self.size -= 1
        return True

        

    def deQueue(self) -> bool:
        dummy = self.dummy
        if self.isEmpty() == True:
            return False
        if dummy.prev == dummy.next:
            dummy.prev = dummy
            self.tail = dummy
        dummy.next = dummy.next.next
        self.dummy = dummy
        self.size += 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            dummy = self.dummy
            return dummy.next.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            dummy = self.dummy
            return dummy.prev.value

    def isEmpty(self) -> bool:
        if self.size == self.init:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.size == 0:
            return True
        return False

    def display(self):
        vals = []
        dummy = self.dummy
        curr_node = dummy.next
        while curr_node:
            if curr_node == dummy:
                break
            vals.append(curr_node.value)
            curr_node = curr_node.next
        return vals

# Your Queue object will be instantiated and called as such:
# obj = Queue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end