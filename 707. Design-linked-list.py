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

    def reverseList(self, head):
        curr_node = head
        prev = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node 
        return prev

    def partition(self, head, x: int):
        """
        insert_node, curr_node, prev_node, dummy_node
        """
        curr_node = head

        dummy1 = dummy_node1 = node(None)
        dummy2 = dummy_node2 = node(None)
        while curr_node:
            if curr_node.value < x and dummy_node1.value == None:
                dummy_node1 = curr_node
                dummy1 = dummy_node1
            elif curr_node.value < x:
                dummy_node1.next = curr_node
                dummy_node1 = dummy_node1.next
            if curr_node.value >= x and dummy_node2.value == None:
                dummy_node2 = curr_node
                dummy2 = dummy_node2
            elif curr_node.value >= x:
                dummy_node2.next = curr_node
                dummy_node2 = dummy_node2.next
            curr_node = curr_node.next
        dummy_node2.next = None
        if dummy1.value is not None:
            dummy_node1.next = dummy2
        else:
            return dummy2
        return dummy1
        
    def display(self):
        mylist = []
        curr_node = self.head
        while curr_node:
            mylist.append(curr_node.value)
            curr_node = curr_node.next
        print(mylist)
        return
    
    def isPalindrome(self, head) -> bool:
        prev = None
        curr_node = head
        original = node(None)
        orig_head = original
        while curr_node:
            if original.value == None:
                original.value = curr_node.value
                curr_node = curr_node.next
                continue
            new_node = node(curr_node.value)
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
        # curr_node = head
        while orig_head and curr_node:
            if curr_node.value != orig_head.value:
                return False
            curr_node = curr_node.next
            orig_head = orig_head.next
        return True
    
    def reverseBetween(self, head, left: int, right: int):
        curr_node = node_head = head
        index = 1
        before = curr_node
        while curr_node and index != left:
            before = curr_node
            curr_node = curr_node.next
            index += 1
        curr_node = head
        while curr_node and index != right+1:
            after = curr_node.next
            curr_node = curr_node.next
            index += 1

        new_list = self.reverseList(before.next)
        after = node(new_list.value)
        before.next = new_list.next
        while new_list.next != None:
            new_list = new_list.next
        new_list.next = after

        return before

    def mergeTwoLists(self, list1, list2) :
        head1 = list1
        head2 = list2
        new_list = node(None)
        new_head = new_list
        while head1 or head2:
            if head1.value <= head2.value:
                new_list.next = node(head1.value)
                new_list = new_list.next
                head1 = head1.next
            else:
                new_list.next = node(head2.value)
                new_list = new_list.next
                head2 = head2.next
            if head1.next == None:
                new_list.next = head2
                break
            elif head2.next == None:
                new_list.next = head1
                break
        new_list.next = None
        return new_head

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

first = MyLinkedList()
first.addAtHead(1)
first.addAtTail(2)
first.addAtTail(4)

second = MyLinkedList()
second.addAtHead(1)
second.addAtTail(3)
second.addAtTail(4)

# mylist.addAtTail(4)
# mylist.addAtTail(5)
# # mylist.addAtTail(2)
# mylist.display()
# print(mylist.isPalindrome(mylist.head))
# new_list = MyLinkedList.mergeTwoLists(self=, first, second)