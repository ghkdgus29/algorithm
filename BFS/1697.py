import collections

MAX = 100000
soobin, younger = map(int, input().split())

distance = [0] * (MAX + 1)
visit = [False] * (MAX + 1)

visit[soobin] = True

queue = collections.deque([soobin])

while queue:
    current_location = queue.popleft()

    if current_location > 0:                                                    # 현재 위치에서 한 칸 뒤로
        if not visit[current_location - 1]:
            distance[current_location - 1] = distance[current_location] + 1
            visit[current_location - 1] = True
            queue.append(current_location - 1)

    if current_location < MAX:                                                  # 현재 위치에서 한 칸 앞으로
        if not visit[current_location + 1]:
            distance[current_location + 1] = distance[current_location] + 1
            visit[current_location + 1] = True
            queue.append(current_location + 1)

    if current_location * 2 <= MAX:                                             # 현재 위치에서 순간이동 (x2)
        if not visit[current_location * 2]:
            distance[current_location * 2] = distance[current_location] + 1
            visit[current_location * 2] = True
            queue.append(current_location * 2)

print(distance[younger])