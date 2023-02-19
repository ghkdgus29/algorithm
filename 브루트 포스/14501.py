def calculate_revenue(day, revenue):
    if day == n:
        revenues.append(revenue)
        return
    elif day > n:
        return

    calculate_revenue(day + period[day], revenue + cost[day])
    calculate_revenue(day + 1, revenue)


n = int(input())
period = []
cost = []
revenues = []

for _ in range(n):
    p, c = map(int, input().split())
    period.append(p)
    cost.append(c)

calculate_revenue(0, 0)

print(max(revenues))
