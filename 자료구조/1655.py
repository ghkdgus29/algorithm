# 주어진 수 중 중간에 있는 수를 말한다.
# 주어진 수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말한다.

# 작은거 { 5 2 1 -99 } <- 최대힙
# 큰거 { 5 7 10 } <- 최소힙

import heapq
import sys

n = int(input())
smaller = []
bigger = []

for _ in range(n):
    a = int(sys.stdin.readline())
    if not smaller:
        smaller.append(-a)

    elif -smaller[0] < a:           # 현재 값이 smaller의 가장 큰 값보다 크면
        heapq.heappush(bigger, a)
        if len(bigger) >= len(smaller) + 1:
            pop = heapq.heappop(bigger)
            heapq.heappush(smaller, -pop)
    else:                           # 현재 값이 smaller 의 가장 큰 값보다 작거나 같으면
        heapq.heappush(smaller, -a)
        if len(smaller) >= len(bigger) + 2:
            pop = -heapq.heappop(smaller)
            heapq.heappush(bigger, pop)

    print(-smaller[0])
