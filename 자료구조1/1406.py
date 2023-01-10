left = list(input())    # 커서 왼쪽
right = []              # 커서 오른쪽

n = int(input())

for _ in range(n):
    ins = input().split()

    if ins[0] == "L":
        if left:
            right.append(left.pop())

    elif ins[0] == "D":
        if right:
            left.append(right.pop())

    elif ins[0] == "B":
        if left:
            left.pop()

    elif ins[0] == "P":
        left.append(ins[1])

print("".join(left) + "".join(right[::-1]))
