class Node:
    def __init__(self, val:int=0, prev:"None|Node"=None, next:"None|Node"=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self, val=0, prev=None, next=None):
        self.head = Node(val, prev, next)
        self.tail = self.head

    def insert_head(self, val):
        dummy = Node(val=val, prev=None, next=self.head)
        if not self.head:
            self.head = dummy
            self.tail = self.head
            return
        self.head.prev = dummy
        self.head = dummy
        
    def insert_tail(self, val):
        dummy = Node(val, self.tail, None)
        if not self.tail:
            self.head = dummy
            self.tail = self.head
            return
        self.tail.next = dummy
        self.tail = self.tail.next

    def remove_head(self):
        if not self.head:
            return
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def remove_tail(self):
        if not self.tail:
            return
        val = self.tail.val
        if self.tail.prev:
            tailNext = self.tail.next
            self.tail = self.tail.prev
            self.tail.next = tailNext
        return val

    def print(self):
        cur = self.head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)

def test():
    dll = DoubleLinkedList()
    dll.remove_head()
    dll.remove_tail()
    dll.insert_head(10)
    dll.insert_head(20)
    dll.insert_head(30)
    dll.insert_head(40)
    dll.insert_tail(200)
    dll.insert_tail(300)
    dll.insert_tail(400)
    dll.insert_tail(500)
    dll.print()
    dll.remove_head()
    dll.remove_tail()
    dll.print()
    print(dll.head.val,dll.tail.val)     # type: ignore


# test()
