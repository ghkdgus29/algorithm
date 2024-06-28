# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pos = []
        length = 0
        current = head
        while current:
            pos.append(current)
            length += 1
            current = current.next

        for i in range(length // k):
            for j in range(k - 1, 0, -1):
                pos[i * k + j].next = pos[i * k + j - 1]

            if i == length // k - 1:            # 마지막 부분
                if length % k == 0:                     # 딱 나눠 떨어질 때
                    pos[i * k].next = None
                else:
                    pos[i * k].next = pos[(i + 1) * k]
            else:
                pos[i * k].next = pos[(i + 1) * k + k - 1]

        return pos[k - 1]
