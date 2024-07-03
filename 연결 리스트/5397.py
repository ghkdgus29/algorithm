for _ in range(int(input())):
    left = []
    right = []
    for ch in input():
        if ch == '<':
            if left:
                right.append(left.pop())
        elif ch == '>':
            if right:
                left.append(right.pop())
        elif ch == '-':
            if left:
                left.pop()
        else:
            left.append(ch)

    print(''.join(left + right[::-1]))
