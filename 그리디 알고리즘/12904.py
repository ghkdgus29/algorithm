given = input()
target = input()

while target:
    if target == given:
        print(1)
        exit()

    if target[-1] == 'A':
        target = target[:-1]
    else:
        target = target[:-1]
        target = target[::-1]

print(0)
