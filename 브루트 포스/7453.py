import collections
import sys

n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

x = []
y = []
for i in range(n):
    for j in range(n):
        x.append(A[i] + B[j])
        y.append(C[i] + D[j])

y_counter = collections.Counter(y)
ans = 0
for each in x:
    ans += y_counter[-each]

print(ans)
