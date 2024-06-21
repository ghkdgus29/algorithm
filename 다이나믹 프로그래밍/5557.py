# 음수 불가, 0~20 범위의 수
# 숫자가 주어졌을 때, 상근이가 만들 수 있는 올바른 등식 개수

# d[i][j] -> i번째까지 확인했고, j는 값임
# d[i][j] = d[i-1][j-a[i]]  <- 현재 값 더하기
#         + d[i-1][j+a[i]]  <- 현재 값 빼기

n = int(input())
a = list(map(int, input().split()))
target = a.pop()
d = [[0] * 21 for _ in range(n - 1)]

d[0][a[0]] = 1
for i in range(1, n - 1):
    for j in range(21):
        if j - a[i] >= 0:
            d[i][j] += d[i - 1][j - a[i]]
        if j + a[i] <= 20:
            d[i][j] += d[i - 1][j + a[i]]

print(d[-1][target])
