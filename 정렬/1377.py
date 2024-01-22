n = int(input())
a = [(int(input()), i) for i in range(n)]
a.sort()

ans = 0
for i in range(n):
    if a[i][1] - i > ans:
        ans = a[i][1] - i

print(ans + 1)
