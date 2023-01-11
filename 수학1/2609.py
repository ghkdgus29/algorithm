def gcd(a, b):              # 유클리드 호제법 사용
    if b <= 0:
        return a

    return gcd(b, a % b)


a, b = map(int, input().split())

GCD = gcd(a, b)
print(GCD)
print(int(a*b/GCD))