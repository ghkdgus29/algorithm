left = list(input())
right = []  # 뒤에 있는게 커서에 가까운 거 (거꾸로)
for _ in range(int(input())):
    command = input()

    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'P':
        left.append(command[2:])
    else:
        if left:
            left.pop()

print(''.join(left + right[::-1]))
