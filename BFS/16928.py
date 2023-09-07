import collections

NOT_VISIT = -1


def bfs(start):
    queue = collections.deque([start])
    distance[start] = 0

    while queue:
        current_node = queue.popleft()

        for dx in range(1, 7):
            if current_node + dx <= 100 and distance[current_node + dx] == NOT_VISIT:
                if current_node + dx in event:                                              # 뱀이나 사다리를 밟은 경우
                    jump = event[current_node + dx]
                    if distance[jump] == NOT_VISIT:
                        distance[jump] = distance[current_node] + 1
                        queue.append(jump)

                else:                                                                       # 안 밟은 경우
                    distance[current_node + dx] = distance[current_node] + 1
                    queue.append(current_node + dx)


ladder_cnt, snake_cnt = map(int, input().split())
event = {}
for _ in range(ladder_cnt + snake_cnt):
    start, end = map(int, input().split())
    event[start] = end

distance = [NOT_VISIT] * 101

bfs(1)

print(distance[100])
