# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        counter = collections.defaultdict(int)
        for head in lists:
            while head != None:
                counter[head.val] += 1
                head = head.next
        keys = sorted(counter.keys())

        root = ListNode()
        current = root
        for key in keys:
            for _ in range(counter[key]):
                current.next = ListNode(key)
                current = current.next
        return root.next

