"""Remove the N-th node from end of linked list (alternative implementation)."""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def total_nodes(head: Optional[ListNode]) -> int:
    total = 0
    while head is not None:
        total += 1
        head = head.next
    return total

def print_list(head: Optional[ListNode]) -> None:
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
print_list(head)
print(total_nodes(head))

pointer_1 = head
iterations = total_nodes(head)-1
if iterations == 0:
    pointer_1 = pointer_1.next
    print_list(pointer_1)
else:    
    while iterations > 0:
        pointer_2 = pointer_1
        pointer_1 = pointer_1.next
        iterations -= 1

    pointer_2.next = pointer_1.next
    print_list(head)