import collections

n = int(input())
a = [0] + list(map(int, input().split()))
d = [0] + [1] * n
idx = [-1] * (n + 1)
ans = collections.deque([])

for i in range(2, n + 1):
    for j in range(1, i):
        if a[j] < a[i] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1
            idx[i] = j

index = d.index(max(d))

while index != -1:              # 역추적
    ans.appendleft(a[index])
    index = idx[index]

print(max(d))
print(*ans)
