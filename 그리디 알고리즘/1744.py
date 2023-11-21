n = int(input())
numbers = [int(input()) for _ in range(n)]

ans = 0

minus_and_zero = []
plus = []

for num in numbers:
    if num <= 0:
        minus_and_zero.append(num)
    elif num == 1:
        ans += 1
    else:
        plus.append(num)

minus_and_zero.sort()
plus.sort(reverse=True)

if len(minus_and_zero) % 2 == 1:
    ans += minus_and_zero.pop()

if len(plus) % 2 == 1:
    ans += plus.pop()

for i in range(0, len(minus_and_zero), 2):
    ans += minus_and_zero[i] * minus_and_zero[i + 1]

for i in range(0, len(plus), 2):
    ans += plus[i] * plus[i + 1]

print(ans)
