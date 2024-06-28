# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        root.next = head
        current = root

        while current.next and current.next.next:
            tail = current.next
            head = current.next.next
            tail.next = head.next
            head.next = tail
            current.next = head
            current = tail

        return root.next
