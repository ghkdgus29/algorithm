import heapq

jewel_cnt, bag_cnt = map(int, input().split())

jewels = []                                         # 보석은 (보석 무게, 보석 가격) 튜플로 저장
for _ in range(jewel_cnt):                          # 보석을 무게순으로 정렬
    weight, price = map(int, input().split())
    jewels.append((weight, price))
jewels.sort(reverse=True)                           # pop 하기 위해 역순으로 뒤집는다. (가벼운 보석이 뒤로간다.)

bags = []
for _ in range(bag_cnt):                            # 들 수 있는 가방 무게를 무게순으로 정렬
    bags.append(int(input()))
bags.sort()

liftable = []                                       # 현재 가방이 들 수 있는 보석들을 담는 최대 힙
total_steal_price = 0
for bag in bags:
    while jewels and bag >= jewels[-1][0]:          # 현재 가방이 담을 수 있는 보석들만 꺼내서 최대힙에 저장
        _, price = jewels.pop()
        heapq.heappush(liftable, -price)            # 가격만 저장 (무게는 상관없음)

    if liftable:
        total_steal_price -= heapq.heappop(liftable)    # 가장 비싼 보석을 최대힙에서 꺼낸다.

print(total_steal_price)
