# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visit = set()
        current = head
        while current:
            if current in visit:
                return current
            visit.add(current)
            current = current.next
