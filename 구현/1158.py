n, k = map(int, input().split())
a = [str(i) for i in range(1, n + 1)]

idx = k - 1
ans = []
while True:
    ans.append(a.pop(idx))
    if not a:
        break
    idx = (idx - 1) % len(a)
    idx = (idx + k) % len(a)

print('<', end="")
print(', '.join(ans), end=">")

