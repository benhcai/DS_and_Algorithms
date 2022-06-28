from reverse_linked_list import reverse_linked_list
from linked_list import Node, LinkedList

ll = LinkedList([1,2,3,4,5])
ll.print_linked_list()
ll.head = reverse_linked_list(ll.head)
ll.print_linked_list()
