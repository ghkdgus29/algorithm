# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        position = {}

        current = head

        length = 0
        while current != None:
            current = current.next
            length += 1

        if length - n - 1 < 0:
            return head.next

        current = head
        for _ in range(length - n - 1):
            current = current.next

        if current.next != None:
            current.next = current.next.next
        else:
            current.next = None
        return head
