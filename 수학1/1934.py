def get_gcd(a, b):
    if b <= 0:
        return a
    return get_gcd(b, a % b)


n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    gcd = get_gcd(a, b)
    print(int(a * b / gcd))
