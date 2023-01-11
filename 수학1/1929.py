total_length = 1000000
prime_check = [True] * (total_length + 1)
prime_check[0] = False
prime_check[1] = False

for i in range(2, total_length + 1):
    if prime_check[i]:
        for j in range(i+i, total_length + 1, i):
            prime_check[j] = False                      # 에라토스테네스의 체 사용

small, big = map(int, input().split())

for i in range(small, big+1):
    if prime_check[i]:
        print(i)

