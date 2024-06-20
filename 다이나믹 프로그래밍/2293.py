# 가치 합이 k원이 되도록 하는 경우의 수

# d[i] -> i원을 만들 때의 경우의 수

n, target = map(int, input().split())
coins = [int(input()) for _ in range(n)]
d = [0] * (target + 1)

d[0] = 1
for c in coins:
    for i in range(target + 1):
        if i - c >= 0:
            d[i] += d[i-c]

print(d[-1])

