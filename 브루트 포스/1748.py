# n < 10 -> d = n
# 10 <= n < 100 -> d = 2n       ex) 9 + 2*(given-9)
# 100 <= n < 1000 -> d = 3n     ex) 9 + 2*90 * 3*(given - 99)

import math

n = int(input())
n_digits = len(str(n))
ans = 0

ans += n_digits * (n - int(math.pow(10, n_digits - 1) - 1))
n_digits -= 1                                                   # 가장 큰 자릿수 계산

while n_digits > 0:
    ans += n_digits * int((math.pow(10, n_digits) - math.pow(10, n_digits - 1)))

    n_digits -= 1

print(ans)
