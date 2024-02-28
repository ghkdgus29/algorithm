import itertools

a, b = input().split()
b = int(b)

ans = -1
for each in itertools.permutations(list(a), len(a)):
    if each[0] == '0':
        continue

    num = int(''.join(each))
    if num >= b:
        continue

    ans = max(ans, num)

print(ans)
