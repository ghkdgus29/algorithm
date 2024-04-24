import collections

target = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
x = []
y = []

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += a[j]
        x.append(sum)

for i in range(m):
    sum = 0
    for j in range(i, m):
        sum += b[j]
        y.append(sum)

ans = 0
y_counter = collections.Counter(y)
for each in x:
    ans += y_counter[target - each]

print(ans)
