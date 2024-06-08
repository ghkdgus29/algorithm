class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}


def dec2bin(n):
    binary = bin(n)[2:]
    return [0] * (32 - len(binary)) + list(map(int, binary))


def bin2dec(b):
    n = 0
    for i in range(32):
        n += b[i] * 2 ** (31 - i)
    return n


n = int(input())
a = list(map(int, input().split()))

root = Node(-1)
ans = -1
for num in a:
    current = root
    binary = dec2bin(num)
    tmp = []
    for bit in binary:                      # search
        if 1 - bit in current.children:
            tmp.append(1)
            current = current.children[1 - bit]
        elif bit in current.children:
            tmp.append(0)
            current = current.children[bit]
        else:
            tmp = [0] * 32
            break
    ans = max(ans, bin2dec(tmp))

    current = root
    for bit in binary:                      # insert
        if bit not in current.children:
            current.children[bit] = Node(bit)
        current = current.children[bit]

print(ans)
