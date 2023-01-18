d = [0] * 12
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 12):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

t = int(input())
for _ in range(t):
    print(d[int(input())])

