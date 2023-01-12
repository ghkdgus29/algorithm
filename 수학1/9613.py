def gcd(a, b):
    if b <= 0:
        return a
    return gcd(b, a % b)


t = int(input())

for _ in range(t):
    numbers = list(map(int, input().split()))
    length = len(numbers)
    gcd_sum = 0

    for i in range(1, length):
        for j in range(i + 1, length):
            gcd_sum += gcd(numbers[i], numbers[j])

    print(gcd_sum)