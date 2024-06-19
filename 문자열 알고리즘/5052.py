# 한 번호가 다른 번호의 접두어라면 일관성 x

class Node:
    def __init__(self, val):
        self.val = val
        self.flag = False
        self.children = {}


t = int(input())
for _ in range(t):
    consistency = True
    n = int(input())
    root = Node(-1)
    numbers = []
    for _ in range(n):
        current = root
        number = input()
        numbers.append(number)
        for ch in number:
            if ch not in current.children:
                current.children[ch] = Node(ch)
            current = current.children[ch]
        current.flag = True

    for number in numbers:
        current = root
        for ch in number[:-1]:
            current = current.children[ch]
            if current.flag:
                consistency = False

    print("YES" if consistency else "NO")



