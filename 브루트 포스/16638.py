n = int(input())
a = list(input())
m = (n + 1) // 2 - 1
ans = float('-inf')
for s in range(1 << m):  # 2^(연산자 개수)
    ok = True
    for i in range(m - 1):
        if (s & (1 << i)) > 0 and (s & (1 << (i + 1))) > 0:  # 연속된 1이 존재하면 false
            ok = False

    if not ok:
        continue

    b = a[:]
    for i in range(m):
        if (s & (1 << i)) > 0:      # 이진수의 i 번째 비트가 1인 경우
            k = 2 * i + 1
            b[k - 1] = '(' + b[k - 1]
            b[k + 1] = b[k + 1] + ')'

    c = ''.join(b)
    temp = int(eval(c))
    ans = max(temp, ans)

print(ans)
