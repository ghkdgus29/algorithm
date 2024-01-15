a = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort()

for x, y in a:
    print(x, y)
