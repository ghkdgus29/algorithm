def go(day):
    if day == n + 1:
        return 0
    if day > n + 1:
        return -10 ** 9
    if d[day] != -1:
        return d[day]

    t1 = go(day + 1)
    t2 = cost[day] + go(day + period[day])
    d[day] = max(t1, t2)
    return d[day]


n = int(input())
period = [0]
cost = [0]
d = [-1] * (n + 1)

for _ in range(n):
    p, c = map(int, input().split())
    period.append(p)
    cost.append(c)

print(go(1))
