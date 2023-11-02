import heapq

n = int(input())

lectures = []
for _ in range(n):
    price, day = map(int, input().split())
    lectures.append((day, price))

lectures.sort()

visitable = []
total_profit = 0
for day in range(10000, 0, -1):
    while lectures and day == lectures[-1][0]:
        _, price = lectures.pop()
        heapq.heappush(visitable, -price)

    if visitable:
        total_profit -= heapq.heappop(visitable)

print(total_profit)
