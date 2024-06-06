def check(flag):
    if flag == LEFT:
        global front
        if len(front) < len(remove):
            return False
        if front[-len(remove):] != remove:
            return False
        for _ in range(len(remove)):
            front.pop()

    else:
        global rear
        if len(rear) < len(remove_reverse):
            return False
        if rear[-len(remove_reverse):] != remove_reverse:
            return False
        for _ in range(len(remove_reverse)):
            rear.pop()

    return True


LEFT = 0
RIGHT = 1

remove = list(input())
remove_reverse = remove[::-1]
given = input()

front = []
rear = []
left = 0
right = len(given) - 1
flag = LEFT

while left <= right:
    if flag == LEFT:
        front.append(given[left])
        left += 1
    else:
        rear.append(given[right])
        right -= 1
    if check(flag):
        flag = 1 ^ flag

for ch in rear[::-1]:
    front.append(ch)
    check(LEFT)

print(''.join(front))
