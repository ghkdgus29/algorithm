# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        prefix_sum_dict = {0: root}

        root.next = head
        current = root.next
        prefix_sum = 0
        while current:
            prefix_sum += current.val
            prefix_sum_dict[prefix_sum] = current
            current = current.next

        current = root
        prefix_sum = 0
        while current:
            prefix_sum += current.val
            current.next = prefix_sum_dict[prefix_sum].next
            current = current.next

        return root.next
