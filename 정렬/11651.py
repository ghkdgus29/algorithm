a = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort(key=lambda i: (i[1], i[0]))

for x, y in a:
    print(x, y)
