#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#

# @lc code=start
class Node:
    def __init__(self, value=None, next =None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.init_size = k
        self.dummy = Node()
        

    def insertFront(self, value: int) -> bool:
        self.value = value
        new_node = Node(self.value)
        dummy = self.dummy
        if self.isFull():
            return False
        elif dummy.next == None: 
            dummy.next = new_node
            new_node.next = dummy
            dummy.prev = new_node
            new_node.prev = dummy
        else:
            head = dummy.next
            new_node.next = head
            new_node.prev = dummy
            head.prev = new_node
            dummy.next = new_node
        print(self.display())
        self.size -= 1
        return True
        

    def insertLast(self, value: int) -> bool:
        self.value = value
        new_node = Node(self.value)
        dummy = self.dummy
        if self.isFull():
            return False
        elif dummy.prev == None:
            dummy.prev = new_node
            new_node.prev = dummy
            dummy.next = new_node
            new_node.next = dummy
        else:
            tail = dummy.prev
            new_node.next = dummy
            new_node.prev = tail
            tail.next = new_node
            dummy.prev = new_node
        self.size -= 1
        return True          


    def deleteFront(self) -> bool:
        dummy = self.dummy
        if self.isEmpty():
            return False
        if dummy.next == dummy.prev:
            dummy.prev = dummy
        dummy.next = dummy.next.next
        dummy.next.prev = dummy
        self.dummy = dummy
        self.size += 1
        return True


    def deleteLast(self) -> bool:
        dummy = self.dummy
        if self.isEmpty():
            return False
        if dummy.next == dummy.prev:
            dummy.prev = dummy
        dummy.prev = dummy.prev.prev
        dummy.prev.next = dummy
        self.dummy = dummy
        self.size += 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.dummy.next.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.dummy.prev.value
        

    def isEmpty(self) -> bool:
        if self.size == self.init_size:
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


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end