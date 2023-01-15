prime_check = [True] * 1000001
prime_check[0] = prime_check[1] = False

for i in range(2, 1000001):                 # 에라토스테네스의 체 사용
    if prime_check[i]:
        for j in range(i + i, 1000001, i):
            prime_check[j] = False


t = int(input())
for _ in range(t):
    n = int(input())

    cnt = 0
    for i in range(n // 2 + 1):
        if prime_check[i] and prime_check[n-i]:
            cnt += 1

    print(cnt)