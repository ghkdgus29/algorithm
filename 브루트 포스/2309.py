def find_fake_dwarf():
    for i in range(8):
        for j in range(i + 1, 9):
            if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
                return dwarf[i], dwarf[j]


dwarf = [int(input()) for _ in range(9)]

fake1, fake2 = find_fake_dwarf()

dwarf.remove(fake1)
dwarf.remove(fake2)
dwarf.sort()

print('\n'.join(map(str, dwarf)))
