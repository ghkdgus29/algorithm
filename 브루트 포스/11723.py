import sys

n = int(input())
bit_mask = 0
for _ in range(n):
    split = sys.stdin.readline().split()

    if split[0] == "add":
        bit_mask = bit_mask | (1 << int(split[1]) - 1)

    elif split[0] == "check":
        if bit_mask & (1 << int(split[1]) - 1):
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')

    elif split[0] == "remove":
        bit_mask = bit_mask & ~(1 << int(split[1]) - 1)

    elif split[0] == "toggle":
        bit_mask = bit_mask ^ (1 << int(split[1]) - 1)

    elif split[0] == "all":
        bit_mask = 2 ** 20 - 1

    elif split[0] == "empty":
        bit_mask = 0

