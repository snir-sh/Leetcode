from typing import Optional

from noeds import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer_1 = head
        iterations = self.total_nodes(head) - n
        if iterations == 0:
            pointer_1 = pointer_1.next
            return pointer_1
        else:
            while iterations > 0:
                pointer_2 = pointer_1
                pointer_1 = pointer_1.next
                iterations -= 1

            pointer_2.next = pointer_1.next
            return head
