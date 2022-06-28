class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, arr):
        self.head = Node(None)
        current = self.head
        for i in arr:
            current.next = Node(i)
            current = current.next
        self.head = self.head.next

    def print_linked_list(self):
        arr = []
        current = self.head
        while current is not None:
            arr.append(current.val)
            current = current.next
        print(arr)