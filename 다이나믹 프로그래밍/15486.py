n = int(input())
t = [0] * n
p = [0] * n
for i in range(n):
    t[i], p[i] = map(int, input().split())
d = [0] * (n + 50)
for i in range(n):
    d[i + t[i]] = max(d[i + t[i]], d[i] + p[i])     # 상담을 하는 경우
    d[i + 1] = max(d[i + 1], d[i])                  # 상담을 하지 않는 경우
print(d[n])
