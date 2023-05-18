from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head 
        self.length = 0

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_at_head(self, val):
        self.length += 1
        new = Node(val)
        if not self.head:
            self.tail = new
        new.next = self.head
        self.head = new
        return self.head

    def insert_at_tail(self, val):
        self.length += 1
        new = Node(val)
        if not self.head:
            self.head = new
            self.tail = new
            return None
        self.tail.next = new
        self.tail = self.tail.next
        return None

    def delete_at_head(self):
        if self.head:
            self.length -= 1
            self.head = self.head.next
        return None

    def delete_at_end(self):
        '''
            Singly linked list requires O(n) traversing
        '''
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None
        self.tail = cur
        return None
    
    def print(self):
        cur = self.head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print(arr)

def test() :
    list = LinkedList()
    list.insert_at_head(5)
    list.delete_at_end()
    list.insert_at_head(9)
    list.insert_at_head(10)
    list.insert_at_head(1)
    print(list.tail.val)
    list.delete_at_end()
    print(list.tail.val)
    list.print()
    list.insert_at_tail(99)
    print(list.tail.val)
    list.delete_at_end()
    print(list.tail.val)
    list.print()
