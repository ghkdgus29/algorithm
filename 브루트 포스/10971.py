def next_permutation(a: list):
    tail = len(a) - 1

    while tail > 0 and a[tail - 1] >= a[tail]:
        tail -= 1

    if tail == 0:
        return False

    change = len(a) - 1
    while a[tail - 1] >= a[change]:
        change -= 1

    a[tail - 1], a[change] = a[change], a[tail - 1]
    a[tail:] = reversed(a[tail:])
    return True


# w[i][j] = i -> j 로 가는 비용

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
ans = 15000000
d = list(range(n))  # 도시번호를 순열로 표현

while True:
    if d[0] != 0:  # 순열의 첫번째 숫자를 0으로 고정, O(N * N!) -> O(N!)
        break

    cost = 0

    for i in range(n - 1):
        if w[d[i]][d[i + 1]] == 0:  # 못가는 도시인 경우
            cost = 15000000
            break
        else:
            cost += w[d[i]][d[i + 1]]

    if w[d[-1]][d[0]] != 0:
        cost += w[d[-1]][d[0]]
        ans = min(ans, cost)

    if not next_permutation(d):
        break

print(ans)
