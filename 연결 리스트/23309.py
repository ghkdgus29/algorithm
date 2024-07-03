import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


n, m = map(int, input().split())
pos = {}
a = list(map(int, input().split()))
pos[a[0]] = Node(a[0])
for i in range(1, n):
    pos[a[i]] = Node(a[i])
    pos[a[i - 1]].next = pos[a[i]]
    pos[a[i]].prev = pos[a[i - 1]]

pos[a[-1]].next = pos[a[0]]
pos[a[0]].prev = pos[a[-1]]

for _ in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'BN':
        fivot = pos[int(command[1])]
        print(fivot.next.val)
        new_node = Node(int(command[-1]))
        pos[new_node.val] = new_node

        new_node.next = fivot.next
        new_node.prev = fivot
        fivot.next = new_node
        new_node.next.prev = new_node
    elif command[0] == 'BP':
        fivot = pos[int(command[1])]
        print(fivot.prev.val)
        new_node = Node(int(command[-1]))
        pos[new_node.val] = new_node

        new_node.next = fivot
        new_node.prev = fivot.prev
        new_node.prev.next = new_node
        fivot.prev = new_node
    elif command[0] == 'CN':
        fivot = pos[int(command[1])]
        del pos[fivot.next.val]
        print(fivot.next.val)
        fivot.next.next.prev = fivot
        fivot.next = fivot.next.next
    else:
        fivot = pos[int(command[1])]
        del pos[fivot.prev.val]
        print(fivot.prev.val)
        fivot.prev.prev.next = fivot
        fivot.prev = fivot.prev.prev
