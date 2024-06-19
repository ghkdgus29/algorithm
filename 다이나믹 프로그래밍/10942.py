import sys

sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [[-1] * n for _ in range(n)]    # d[i][j] -> i번째 문자열 ~ j번째 문자열까지가 팰린드롬이면 1 아니면 0


def go(i, j):
    if i == j:                  # 1글자는 무조건 팰린드롬
        return 1
    elif i + 1 == j:            # 2글자는 둘이 같아야 팰린드롬
        if a[i] == a[j]:
            return 1
        else:
            return 0

    if d[i][j] != -1:           # 이미 검사한 경우
        return d[i][j]

    if a[i] != a[j]:            # 문자열 s의 i ~ j 번째 부분 문자열이 팰린드롬이 되려면 s[i] == s[j] 이고, s[i+1] ~ s[j-1] 이 팰린드롬이여야 한다.
        d[i][j] = 0
    else:
        d[i][j] = go(i + 1, j - 1)
    return d[i][j]


for _ in range(int(input())):
    s, e = map(int, sys.stdin.readline().split())
    print(go(s - 1, e - 1))
