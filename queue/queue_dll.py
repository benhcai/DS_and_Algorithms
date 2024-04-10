from Double_Linked_List import DoubleLinkedList

class Queue:
    def __init__(self):
        self.queue = DoubleLinkedList() 

    def enqueue(self, val):
        self.queue.insert_head(val)
    
    def dequeue(self):
        return self.queue.remove_head()

    def peek(self):
        if self.queue.head:
            return self.queue.head
        return None

    def print(self):
        self.queue.print()

def test():
    queue = Queue()
    queue.dequeue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.print()

test()
