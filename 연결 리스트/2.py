# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        current = root
        next_val = 0
        while l1 != None and l2 != None:
            current.next = ListNode((l1.val + l2.val + next_val) % 10)
            current = current.next
            next_val = (l1.val + l2.val + next_val) // 10
            l1 = l1.next
            l2 = l2.next

        if l1 != None:
            while l1 != None:
                current.next = ListNode((l1.val + next_val) % 10)
                current = current.next
                next_val = (l1.val + next_val) // 10
                l1 = l1.next
        else:
            while l2 != None:
                current.next = ListNode((l2.val + next_val) % 10)
                current = current.next
                next_val = (l2.val + next_val) // 10
                l2 = l2.next

        if next_val > 0:
            current.next = ListNode(next_val)

        return root.next
