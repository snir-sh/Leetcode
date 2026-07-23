# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from noeds import ListNode

def print_list(head: Optional[ListNode]) -> None:
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

"""Merge multiple sorted linked lists into one sorted list."""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = ListNode(0)
        head1 = list1
        head2 = list2
        merged_head_pointer = merged_head
        
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                merged_head_pointer.next = head1
                head1 = head1.next
            else:
                merged_head_pointer.next = head2
                head2 = head2.next
            merged_head_pointer = merged_head_pointer.next
        return merged_head.next
    

s = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
merged_list = s.mergeTwoLists(list1, list2)

# Print the merged list
print_list(merged_list)
