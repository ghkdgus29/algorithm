class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.flag = False


n, m = map(int, input().split())
root = Node(-1)
for _ in range(n):
    current = root
    s = input()

    for ch in s:
        if ch not in current.children:
            current.children[ch] = Node(ch)
        current = current.children[ch]
    current.flag = True

ans = 0
for _ in range(m):
    current = root
    s = input()
    flag = True
    for ch in s:
        if ch not in current.children:
            flag = False
            break
        current = current.children[ch]
    if flag:
        ans += 1

print(ans)
