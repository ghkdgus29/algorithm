# 공격 횟수의 최솟값 구하기

# d[i][j][k] = min(d[i+9][j+3][k+1] ... ) + 1

n = int(input())
scv = list(map(int, input().split()))
while len(scv) < 3:
    scv += [0]

d = [[[float('inf')] * 61 for _ in range(61)] for _ in range(61)]


def go(i, j, k):
    if i < 0:
        return go(0, j, k)
    if j < 0:
        return go(i, 0, k)
    if k < 0:
        return go(i, j, 0)

    if i == 0 and j == 0 and k == 0:
        return 0

    ans = d[i][j][k]
    if ans != float('inf'):
        return ans
    ans = min(go(i - 1, j - 3, k - 9), go(i - 1, j - 9, k - 3),
              go(i - 3, j - 1, k - 9), go(i - 3, j - 9, k - 1),
              go(i - 9, j - 1, k - 3), go(i - 9, j - 3, k - 1)) + 1
    d[i][j][k] = ans
    return d[i][j][k]


print(go(scv[0], scv[1], scv[2]))
