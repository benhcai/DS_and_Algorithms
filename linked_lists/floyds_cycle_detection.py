class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, val=0, next=None):
        self.head = LinkNode(val, next) 

    def create_cycle(self, length, intersection):
        current = self.head
        prev = LinkNode(next=self.head)
        for i in range(self.head.val+1, length):
            current.next = LinkNode(i)
            prev = current
            current = current.next
        intersect = self.head
        for i in range(1, intersection):
            intersect = intersect.next
        prev.next = intersect
    
    def show(self):
        nodes = []
        current = self.head
        for i in range(14):
            if not current:
                break
            nodes.append(current.val)
            current = current.next
        print(nodes)

ll = LinkedList(1)
ll.create_cycle(8,4)
ll.show()

class CycleDetection:
    @staticmethod
    def isCycle(head):
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        if slow:
            return True
        return False

    @staticmethod
    def findIntersecton(head):
        if not head or not head.next:
            return False
        slow = head.next
        fast = head.next.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        if fast == None:
            return False
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow.val
    
    @staticmethod
    def findIntersection2(head):
        '''
            While True-Break is used to simulate a do-while loop,
            where the logic runs firstly runs once, then the condition is checked.
        '''
        if not head:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast == None or fast.next == None:
            return False
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow.val


print('Cycle exists: ', CycleDetection.isCycle(ll.head))
print('Intersection @: ', CycleDetection.findIntersecton(ll.head))
print('Intersecton 2@: ', CycleDetection.findIntersection2(ll.head))

my = LinkedList()
curr = my.head
curr.next = LinkNode(1)
curr = curr.next
curr.next = LinkNode(2)
my.show()

print('Cycle exists: ', CycleDetection.findIntersection2(my.head))
