# d[n] = d[n-2]*3 + d[n-4]*2 + ... + d[2]*2 + 2

# d[4] = d[2]*3 + 2
# d[6] = d[4]*3 + 2 + d[2]*2
n = int(input())

d = [0] * 31

d[2] = 3
d[4] = 11

for i in range(6, n + 1, 2):
    d[i] += d[i - 2] * 3 + 2
    for j in range(4, i - 2 + 1, 2):
        d[i] += d[i - j] * 2

print(d[n])
